
from generation.ModelGenerator import ModelGenerator
from transformers import pipeline, AutoTokenizer
import torch

class CodeLlamaModel(ModelGenerator):
    def __init__(self, model="codellama/CodeLlama-7b-hf"):
        self.model = model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model)

        self.pipeline = pipeline(
            "text-generation",
            model=self.model,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def generate(self, task) -> str:
        prompt = task.prompt
        response = self.pipeline(
            prompt,
            do_sample=True,
            top_k=10,
            temperature=0.1,
            num_return_sequences=1,
            eos_token_id=self.tokenizer.eos_token_id,
            max_length=1024,
        )

        for seq in response:
            print(f"Result: {seq['generated_text']}")

        return response[0]["generated_text"]

    def extract_code(self, task, content) -> list:
        return content
