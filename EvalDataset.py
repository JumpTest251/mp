import json
import pandas as pd


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

    def to_pd(self):
        """
        Convert the dataset to a pandas dataframe
        """
        return pd.DataFrame(self.data)
