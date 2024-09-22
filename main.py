from EvalDataset import EvalDataset

if __name__ == '__main__':
    dataset = EvalDataset()
    dataset.load_data()
    print(dataset.to_pd().head(10))