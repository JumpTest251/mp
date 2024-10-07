from EvalDataset import EvalTask
from generation.ModelGenerator import ModelGenerator
from openai import OpenAI
import os
import re
import json


class OpenAIGenerator(ModelGenerator):
    def __init__(self, model="gpt-4o-mini", base_url=None, client=None):
        self.model = model
        if not client:
            with open("config.json", "r") as f:
                api_key = json.load(f)["openai_key"]
                os.environ["OPENAI_API_KEY"] = api_key

            if base_url:
                self.client = OpenAI(base_url=base_url)
            else:
                self.client = OpenAI()
        else:
            self.client = client


    def generate(self, task: EvalTask) -> str:
        prompt = task.prompt
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional python programmer, only respond with code."},
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )
        #print(response)
        return response.choices[0].message.content

    def extract_code(self, task: EvalTask, content) -> list:
        if task.language == "python":
            code_blocks = re.findall(r'```python(.*?)```', content, re.DOTALL)
        else:
            code_blocks = re.findall(r'```javascript(.*?)```', content, re.DOTALL)

        if all(not block.strip() for block in code_blocks):
            code_blocks.append(content)

        return code_blocks

class OllamaGenerator(OpenAIGenerator):
    def __init__(self, model="codellama:7b-instruct"):
        self.model = model
        self.client = OpenAI(
            base_url="http://localhost:11434/v1/",
            api_key="ollama"
        )
    def extract_code(self, task: EvalTask, content) -> list:
        code_blocks = re.findall(r'```(.*?)```', content, re.DOTALL)
        if all(not block.strip() for block in code_blocks):
            code_blocks.append(content)

        return code_blocks