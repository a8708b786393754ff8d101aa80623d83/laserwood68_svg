from xml.etree import ElementTree as ET


class BaseModel:
    """Classe de base de tout les models."""

    def __init__(self) -> None:
        """Methode constructrice."""

        # ET.register_namespace("","http://www.w3.org/2000/svg")
        self.filename = None
        self.tree = None

    def set_filename(self, file: str):

        self.filename = file

    def parse(self, encode: str = 'ISO-8859-5') -> None:
        """Parse le fichier, il se peut qu'il l'analyse de fichier echoue, dans ce cas on le parse avec XMLParser

        Args:
            encoding (str, optional): type d'encodage. Defaults to 'utf8'.
        """

        self.tree = ET.parse(
            self.filename,  parser=ET.XMLParser(encoding=encode))

    def split_namespace(self, tag: str):
        """Retourne le tag sans le namspace

        Args:
            tag (str): balise xml

        Returns:
            str: tag
        """

        return tag.split('}')[1]

    def root(self) -> ET.Element:
        """Retourne le noeud root

        Returns:
            ET.Element: Element root
        """

        return self.tree.getroot()

    def get_all_tag(self) -> list[str]:
        """Renvoie tout les tag du neoud root

        Returns:
            list[str]: liste des tags
        """

        return [element.tag for element in self.root().iter()]

    def get_all_attrib(self) -> dict[str, str]:
        """Renvoie tout les attributs qui sont dans le neoud du root

        Returns:
            dict[str, str]: dictionnaire d'attributs
        """

        return [element.attrib for element in self.root().iter()]

    def write(self, name: str) -> None:
        """Ecriture d'un fichier, d'un nouveau si le nom est donnée ou d'une sauvegarde

        Args:
            name (str): nom du nouveau fichier
        """

        if name:
            self.tree.write(name)
        else:
            self.tree.write(self.filename)
