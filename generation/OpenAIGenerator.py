from generation.ModelGenerator import ModelGenerator
from openai import OpenAI
import os
import re

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()

class OpenAIGenerator(ModelGenerator):
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def generate(self, task) -> str:
        prompt = task["prompt"]
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a professional programmer, only respond with code."},
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )
        print(response)
        code = self.extract_code(response.choices[0].message.content)
        self.write_to_file(code)
        return response.choices[0].message.content

    def extract_code(self, content):
        code_blocks = re.findall(r'```python(.*?)```', content, re.DOTALL)
        if all(not block.strip() for block in code_blocks):
            code_blocks.append(content)

        return code_blocks

    def write_to_file(self, code_blocks):
        with open("output.py", "w") as f:
            for code in code_blocks:
                f.write(code.strip())
