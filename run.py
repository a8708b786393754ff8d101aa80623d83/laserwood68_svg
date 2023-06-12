#! /usr/bin/python3
from src.views.AppView import AppView
from src.views.MainFrame import MainFrame

app = AppView()
main_frame = MainFrame(app)

main_frame.number()
main_frame.title()
main_frame.validate()
main_frame.preview()


app.mainloop()