from .BaseModel import BaseModel

class LayerModel(BaseModel): 
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        
        