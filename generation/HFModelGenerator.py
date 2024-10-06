from EvalDataset import EvalTask
from generation.ModelGenerator import ModelGenerator
from openai import OpenAI
import os
import re
import json
import requests

API_URL = "https://api-inference.huggingface.co/models/"

class HFModelGenerator(ModelGenerator):
    def __init__(self, model="codellama/CodeLlama-7b-hf"):
        self.model = model
        with open("config.json", "r") as f:
            self.api_key = json.load(f)["hf_key"]


    def generate(self, task: EvalTask) -> str:
        prompt = task.prompt
        payload = {
            "inputs" : prompt,
            "parameters": {"temperature": 0.1}
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(API_URL + self.model, json=payload, headers=headers)
        print(response.json())
        return "b"

    def extract_code(self, task: EvalTask, content) -> list:
        return ["a"]

