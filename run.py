#! /usr/bin/python3
from src.views.AppView import AppView
from src.views.MainFrame import MainFrame

from src.controllers.ElementController import ElementController
from src.controllers.LayerController import LayerController

from src.models.ElementModel import ElementModel
from src.models.LayerModel import LayerModel

app = AppView()
main_frame = MainFrame(app)


main_frame.number()
main_frame.title()
main_frame.validate()
main_frame.preview()

element = ElementController(main_frame, ElementModel)

app.mainloop()
