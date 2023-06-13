from .BaseController import BaseController


class ElementController(BaseController):
    def __init__(self, frame, model) -> None:
        super().__init__(frame, model)

    def cut(self): 
        title = self.frame.title_.get()
        id = self.frame.numbers_.get()

    def add(self): pass
