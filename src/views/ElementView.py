import tkinter as ttk


class ElementView(ttk.Frame):
    def __init__(self) -> None:
        self.root = None

    def set_root(self, root: ttk.Tk):
        self.root = root

    def add(self, funct_callback: function):
        self.button_add = ttk.Button(
            self.root, text='Ajoutée', command=funct_callback).grid()
