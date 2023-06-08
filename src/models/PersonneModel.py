from .BaseModel import BaseModel


class PersonneModel(BaseModel):
    def __init__(self, filename: str, id: int) -> None:
        super().__init__(filename)
        self.id = id

    def get_node_g(self):
        """Renvoie le neoud xml du personnage

        Returns:
            _type_: _description_
        """
        return self.root().find(f'.*[@id="g{self.id}"]')
