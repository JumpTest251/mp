from openai import models

from EvalDataset import EvalDataset
from generation.CodeLlamaModel import CodeLlamaModel
from generation.OpenAIGenerator import OpenAIGenerator
from generation.evaluation import Evaluator

if __name__ == '__main__':
    dataset = EvalDataset()
    dataset.load_data()
    print(dataset.to_pd().head(10))

    evaluator = Evaluator(model=CodeLlamaModel())
    evaluator.run_evaluation()