import tkinter as ttk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path


class MainFrame(ttk.Frame):
    def __init__(self, root: ttk.Tk):
        super().__init__()
        self.numbers_ = ttk.StringVar()
        self.title_ = ttk.StringVar()

        self.root = root
        self.filetype = (
            ('fichier svg', '*.svg'),
            ('fichier xml', '*.xml'),
            ('Tout les fichiers', '*.*')
        )

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

    def add_file(self):

        self.button_add = ttk.Button(
            self.root, text='Ajoutée l\'image svg', command=self.__add_file).grid()

    def __add_file(self):
        file = filedialog.askopenfile(
            title='Ajoutée un fichier svg',
            initialdir=str(Path.home()),
            filetypes=self.filetype
        )

        messagebox.showinfo(title='Seléctionnée un fichier', message=file)

    def preview(self):

        self.button_preview = ttk.Button(
            self.root, text="Prévisualisée").grid()

    def error(self, title: str, message: str):

        messagebox.showerror(title, message)

    def validate_information(self):

        messagebox.showinfo('Validée', 'La validation a bien été effectuée')
