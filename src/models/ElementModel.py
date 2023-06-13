from .BaseModel import BaseModel


class ElementModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()
        self.id = None

    def set_id(self, id: int | str) -> None:
        """Initialise l'id a l'attribut id

        Args:
            id (int | str): id de la balise html
        """
        
        self.id = id

    def get_node_g(self):
        """Renvoie le neoud xml du personnage

        Returns:
            _type_: _description_
        """
        return self.root().find(f'.*[@id="g{self.id}"]')
