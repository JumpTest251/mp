from EvalDataset import EvalDataset
from generation.OpenAIGenerator import OpenAIGenerator

if __name__ == '__main__':
    dataset = EvalDataset()
    dataset.load_data()
    print(dataset.to_pd().head(10))

    generator = OpenAIGenerator()
    for prompt in dataset.prompts():
        print(generator.generate({"prompt": prompt}))
