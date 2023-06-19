import re
from .BaseController import BaseController
from tkinter import END as TK_END


class ElementController(BaseController):
    def __init__(self, frame, model) -> None:
        super().__init__(frame, model)

    def is_number(self, id: str | int) -> None:

        return re.match('^[0-9]*$', id)

    def cut(self) -> None:
        id = self.frame.numbers_.get()
        title = self.frame.title_.get()
        if self.is_number(id):
            if not title:  # NOTE okau y a rien dans title
                self.frame.error('Erruer', 'Entrez un titre')
            else:
                self.frame.validate_information()
        else:
            self.frame.error('Erruer définition',
                             'Entrez le numero de l\'element et un titre')

    def add(self): pass
    
    def reset(self): 
        self.frame.entry_num_frame.delete(0, TK_END)
        self.frame.entry_font.delete(0, TK_END)
        self.frame.entry_taille.delete(0, TK_END)
        self.frame.entry_taille_police.delete(0, TK_END)
