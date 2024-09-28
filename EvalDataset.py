import json
import pandas as pd

class EvalTask:
    def __init__(self, task):
        self.prompt = task["prompt"]
        self.id = task["taskId"]
        self.language = task["language"]

class EvalDataset:
    def __init__(self, path = "data/dataset.json"):
        self.path = path
        self.data = []

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

    def to_pd(self):
        """
        Convert the dataset to a pandas dataframe
        """
        return pd.DataFrame(self.data)
