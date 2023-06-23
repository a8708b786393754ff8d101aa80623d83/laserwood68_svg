from .BaseController import BaseController


class LayerController(BaseController):
    def __init__(self, frame, model) -> None:
        super().__init__(frame, model)
        
    def add(self): pass 
    
    def set_title(self, title: str): 
        
        self.model.title = title
        
    