from EvalDataset import EvalTask
from generation.ModelGenerator import ModelGenerator
from openai import OpenAI
import os
import re
import json


class OpenAIGenerator(ModelGenerator):
    def __init__(self, model="gpt-4o-mini"):
        self.model = model
        with open("config.json", "r") as f:
            api_key = json.load(f)["openai_key"]
            os.environ["OPENAI_API_KEY"] = api_key

        self.client = OpenAI()


    def generate(self, task: EvalTask) -> str:
        prompt = task.prompt
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional programmer, only respond with code."},
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )
        return response.choices[0].message.content

    def extract_code(self, task: EvalTask, content) -> list:
        if task.language == "python":
            code_blocks = re.findall(r'```python(.*?)```', content, re.DOTALL)
        else:
            code_blocks = re.findall(r'```javascript(.*?)```', content, re.DOTALL)

        if all(not block.strip() for block in code_blocks):
            code_blocks.append(content)

        return code_blocks

