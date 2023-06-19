#! /usr/bin/python3
from src.views.AppView import AppView
from src.views.MainFrame import MainFrame

from src.controllers.ElementController import ElementController
from src.controllers.LayerController import LayerController

from src.models.ElementModel import ElementModel
from src.models.LayerModel import LayerModel

app = AppView()
main_frame = MainFrame(app)
element_model = ElementModel()

element = ElementController(main_frame, element_model)


main_frame.title()
main_frame.frame()
main_frame.font()
main_frame.taille()
main_frame.number_personnage()
main_frame.taille_police()
main_frame.add_file()
main_frame.validate(element.cut)
main_frame.preview()
main_frame.reset_button()


app.mainloop()
