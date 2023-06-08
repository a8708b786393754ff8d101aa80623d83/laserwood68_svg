from .BaseModel import BaseModel

class PersonneModel(BaseModel): 
    def __init__(self, filename: str, id: int) -> None:
        super().__init__(filename)
        self.id = id
        
    
        
    