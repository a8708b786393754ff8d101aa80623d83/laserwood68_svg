import tkinter as ttk


class AppView(ttk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title('LaserWood SVG')
        self.geometry('800x900')
        self.config(bg='black')
