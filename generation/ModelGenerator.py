from abc import ABC, abstractmethod

class ModelGenerator(ABC):

    @abstractmethod
    def generate(self, task) -> str:
        pass