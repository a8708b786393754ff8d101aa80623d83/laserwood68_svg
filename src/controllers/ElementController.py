import re
from .BaseController import BaseController


class ElementController(BaseController):
    def __init__(self, frame, model) -> None:
        super().__init__(frame, model)

    def is_number(self, id: str | int) -> None:

        return re.match('^[0-9]*$', id)

    def cut(self) -> None:
        id = self.frame.numbers_.get()
        if not self.is_number(id):
            self.frame.error('Erruer de définition de l\'id',
                             'Entrez le numero de l\'element')

        title = self.frame.title_.get()

    def add(self): pass
