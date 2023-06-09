from .BaseModel import BaseModel

class CadreModel(BaseModel): 
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        
        