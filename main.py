
from EvalDataset import EvalDataset
from generation.CodeLlamaModel import CodeLlamaModel
from generation.HFModelGenerator import HFModelGenerator
from generation.OpenAIGenerator import OpenAIGenerator, OllamaGenerator
from generation.evaluation import Evaluator, Prompter

if __name__ == '__main__':
    dataset = EvalDataset()
    dataset.load_data()
#    print(dataset.tasks()[19])

    evaluator = Evaluator(model=OpenAIGenerator(), prompter=Prompter(), output_path="output/default/gpt4")
    evaluator.run_evaluation()