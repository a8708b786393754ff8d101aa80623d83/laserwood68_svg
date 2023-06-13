import re
from .BaseController import BaseController


class ElementController(BaseController):
    def __init__(self, frame, model) -> None:
        super().__init__(frame, model)

    def is_number(self, id: str | int):

        return re.match('^[0-9]*$', id)

    def cut(self):
        id = self.frame.numbers_.get()
        if self.is_number(id):
            print("C'est un nombre")

        title = self.frame.title_.get()

    def add(self): pass
