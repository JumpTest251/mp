import json
import pandas as pd


class EvalTask:
    def __init__(self, task):
        self.prompt = task["prompt"]
        self.id = task["taskId"]
        self.language = task["language"]
        self.type = task["type"]

    def __str__(self):
        return f"Task ID: {self.id}, Prompt: {self.prompt}, Language: {self.language}"


class EvalDataset:
    def __init__(self, path="data/dataset.json", data=None):
        if data is None:
            self.data = []
        self.path = path

    def load_data(self):
        """
        Load the dataset from a json file
        """
        with open(self.path, 'r') as f:
            data = json.load(f)
            self.data = data

    def prompts(self):
        """
        Return the prompts in the dataset
        """
        return [d["prompt"] for d in self.data]

    def tasks(self):
        """
        Return the tasks in the dataset
        """
        return [EvalTask(d) for d in self.data]

    def filter(self, language=None, instruct_type=None):
        """
        Filter the dataset by language and instruction type
        """
        self.data = [d for d in self.data if (language is None or d["language"] == language) and (
                instruct_type is None or d["type"] == instruct_type)]
        return self

    def to_pd(self):
        """
        Convert the dataset to a pandas dataframe
        """
        return pd.DataFrame(self.data)
