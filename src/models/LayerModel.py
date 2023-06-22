from .BaseModel import BaseModel


class LayerModel(BaseModel):
    def __init__(self) -> None:
        super().__init__()
        self.title = None
        self.name = None
        self.font = None
        self.size = None
        self.size_policy = None

        self.header_xml = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        self.header_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="800 800">'
        self.text_svg = '<text xmlns="http://www.w3.org/2000/svg" xml:space="preserve" style="font-size:1.6679px;line-height:30;font-family:Bahnschrift;-inkscape-font-specification:Bahnschrift;letter-spacing:0;word-spacing:0;writing-mode:lr-tb;stroke-width:.0208486" x="721.761" y="398.708"></text>'
        self.tspan_svg = '<tspan x="721.761" y="398.708" style="stroke-width:.0208486"></tspan>'
        self.svg_closed = '</svg>'

