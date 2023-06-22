import re
from .BaseController import BaseController
from tkinter import END as TK_END


class ElementController(BaseController):
    def __init__(self, frame, model) -> None:
        super().__init__(frame, model)

    def is_number(self, id: str | int) -> None:

        return re.match('^[0-9]*$', id)

    def validate(self) -> None:
        if self.frame.title_.get():
            return True
        return False
    
    def add(self): pass
    
    def reset(self): 
        self.frame.entry_font.delete(0, TK_END)
        self.frame.entry_taille.delete(0, TK_END)
        self.frame.entry_taille_police.delete(0, TK_END)
        
        for i in range(len(self.frame.personnages['num'])): 
            self.frame.personnages['num'][i].delete(0, TK_END)
            self.frame.personnages['name'][i].delete(0, TK_END)
