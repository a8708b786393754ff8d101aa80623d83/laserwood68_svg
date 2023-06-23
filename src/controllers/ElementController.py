import re
from .BaseController import BaseController
from tkinter import END as TK_END
from src.views import succes, error


class ElementController(BaseController):
    def __init__(self, frame, model) -> None:
        super().__init__(frame, model)

    def is_number(self, id: str | int) -> bool:

        return re.match('^[0-9]*$', id)

    def validate(self) -> None:
        error_ = False
        for name, number in zip(self.frame.names, self.frame.numbers):
            if (name.get() != '' and number.get() == '') or (number.get() != '' and name.get() == ''):
                error_ = True
            if number.get() != '' and not self.is_number(number.get()):
                error_ = True

        if self.frame.title_.get() == '':
            error_ = True

        if error_:
            error('Erruer', 'Veuillez entrez les bonnes valeurs')
        else: 
            succes()

    def add(self): pass

    def reset(self):
        self.frame.entry_font.delete(0, TK_END)
        self.frame.entry_taille.delete(0, TK_END)
        self.frame.entry_taille_police.delete(0, TK_END)

        self.frame.entry_title.delete(0, TK_END)

        for i in range(len(self.frame.personnages['num'])):
            self.frame.personnages['num'][i].delete(0, TK_END)
            self.frame.personnages['name'][i].delete(0, TK_END)
