
from EvalDataset import EvalDataset
from generation.CodeLlamaModel import CodeLlamaModel
from generation.HFModelGenerator import HFModelGenerator
from generation.OpenAIGenerator import OpenAIGenerator
from generation.evaluation import Evaluator, Prompter

if __name__ == '__main__':
    dataset = EvalDataset()
    dataset.load_data()
    print(dataset.to_pd().head(10))

    evaluator = Evaluator(model=HFModelGenerator(), prompter=Prompter(), name="default")
    evaluator.run_evaluation()