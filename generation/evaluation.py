from EvalDataset import EvalDataset
from generation.ModelGenerator import ModelGenerator
from utils.code_utils import write_to_file
from tqdm import tqdm

class Prompter:
    def prompt_model(self, model, prompt):
        return model.generate(prompt)

class Evaluator:
    def __init__(self, model: ModelGenerator, prompter: Prompter, name="defaults", output_path = "output/", data = None):
        self.model = model
        if data:
            self.data = data
        else:
            self.data = EvalDataset()
            self.data.load_data()

        self.name = name
        self.output_path = output_path
        self.prompter = prompter

    def run_evaluation(self, n = 1):
        tasks = self.data.filter(language="python").tasks()
        for task in tqdm(tasks):
            for i in range(n):
                content = self.prompter.prompt_model(self.model, task)
                code = self.model.extract_code(task, content)
                #output_location = f"{self.output_path}/{self.name}/{task.id}/"
                output_location = f"{self.output_path}/{task.id}/"
                write_to_file(output_location, i, task.language, code)


