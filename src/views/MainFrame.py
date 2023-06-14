import tkinter as ttk
from tkinter import messagebox


class MainFrame(ttk.Frame):
    def __init__(self, root: ttk.Tk):
        super().__init__()
        self.numbers_ = ttk.StringVar()
        self.title_ = ttk.StringVar()

        self.root = root

    def number(self):
        self.label_number = ttk.Label(
            self.root, text='Numero du personnage: ').grid(row=0)
        self.listbox = ttk.Entry(
            self.root, textvariable=self.numbers_).grid(row=0, column=1)

    def title(self):
        self.label_title = ttk.Label(
            self.root, text='Titre', width=20).grid(row=1)
        self.entry_title = ttk.Entry(
            self.root, textvariable=self.title_).grid(row=1, column=1)

    def validate(self, funct_callback):
        self.button_validate = ttk.Button(
            self.root, text='Validée', command=funct_callback).grid()

    def preview(self):
        self.button_preview = ttk.Button(
            self.root, text="Prévisualisée").grid()

    def error(self, title: str, message: str):
        messagebox.showerror(title, message)
        
    def validate_information(self): 
        
        messagebox.showinfo('Validée', 'La validation a bien été effectuée')
