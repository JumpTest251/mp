from openai import models

from EvalDataset import EvalDataset
from generation.OpenAIGenerator import OpenAIGenerator
from generation.evaluation import Evaluator

if __name__ == '__main__':
    dataset = EvalDataset()
    dataset.load_data()
    print(dataset.to_pd().head(10))

    evaluator = Evaluator(model=OpenAIGenerator())
    evaluator.run_evaluation()