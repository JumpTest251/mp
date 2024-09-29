from abc import ABC, abstractmethod



class ModelGenerator(ABC):

    @abstractmethod
    def generate(self, task) -> str:
        pass

    @abstractmethod
    def extract_code(self, task, content) -> list:
        pass
