from .BaseModel import BaseModel

class PersonneModel(BaseModel): 
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        
    