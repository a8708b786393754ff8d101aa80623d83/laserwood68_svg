from abc import abstractclassmethod
from abc import ABC


class BaseController(ABC):
    def __init__(self, frame, model) -> None:
        self.frame = frame
        self.model = model

    @abstractclassmethod
    def add(self): pass
