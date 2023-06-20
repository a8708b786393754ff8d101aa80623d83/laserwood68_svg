import tkinter as ttk
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path


class MainFrame(ttk.Frame):
    def __init__(self, root: ttk.Tk):
        super().__init__()
        self.title_ = ttk.StringVar()
        self.num_frame_ = ttk.StringVar()
        self.font_ = ttk.StringVar()
        self.taille_ = ttk.StringVar()
        self.taille_police_ = ttk.StringVar()

        self.root = root
        self.filetype = (
            ('fichier svg', '*.svg'),
            ('fichier xml', '*.xml'),
            ('Tout les fichiers', '*.*')
        )

        self.personnages = {'num': [], 'name': []}
        self.names = [] 
        self.numbers = []

    def title(self):
        label_title = ttk.Label(
            self.root, text='Titre', width=20).grid(row=1)
        self.entry_title = ttk.Entry(
            self.root, textvariable=self.title_).grid(row=1, column=1)

    def frame(self):
        label_num_frame = ttk.Label(self.root, text='Numero frame', width=20).grid(row=2)
        self.entry_num_frame = ttk.Entry(
            self.root, textvariable=self.num_frame_)

        self.entry_num_frame.grid(row=2, column=1)

    def font(self):
        label_font = ttk.Label(self.root, text='Font', width=20).grid(row=3)
        self.entry_font = ttk.Entry(self.root, textvariable=self.font_)

        self.entry_font.insert(0, '1')
        self.entry_font.grid(row=3, column=1)

    def taille(self):
        label_taille = ttk.Label(self.root, text='Taille', width=20).grid(row=4)
        self.entry_taille = ttk.Entry(
            self.root, textvariable=self.taille_)

        self.entry_taille.insert(0, 10)
        self.entry_taille.grid(row=4, column=1)

    def number_personnage(self):
        row_label_number = 5
        column_label_number = 0

        row_entry_number = 5
        column_entry_number = 1

        row_label_name = 5
        column_label_name = 2
 
        row_entry_name = 5
        column_entry_name = 3

        for _ in range(0, 8):
            name = ttk.StringVar()
            number = ttk.StringVar()
            
            label_number = ttk.Label(
                self.root, text='Numero du personnage: ').grid(row=row_label_number, column=column_label_number)
            label_name = ttk.Label(
                self.root, text='Prenom: ').grid(row=row_label_name, column=column_label_name)

            entry_number = ttk.Entry(self.root, textvariable=number)
            entry_name = ttk.Entry(self.root, textvariable=name)

            entry_number.grid(row=row_entry_number, column=column_entry_number)
            entry_name.grid(row=row_entry_name, column=column_entry_name)
            
            self.personnages['name'].append(entry_name)
            self.personnages['num'].append(entry_number)
            
            self.names.append(name)
            self.numbers.append(number)
            
            row_label_number += 1
            row_label_name += 1

            row_entry_name += 1
            row_entry_number += 1
            

    def taille_police(self):
        label_taille_police = ttk.Label(self.root, text='Taille de la police', width=20).grid(row=13)
        self.entry_taille_police = ttk.Entry(self.root, textvariable=self.taille_police_)
        self.entry_taille_police.insert(0, 10)
        self.entry_taille_police.grid(row=13, column=1)

    def reset_button(self, funct_callback):
        self.button_reset = ttk.Button(self.root, text='RESET', command=funct_callback, width=20).grid(row=14, column=2)

    def validate(self, funct_callback):

        self.button_validate = ttk.Button(
            self.root, text='Validée', command=funct_callback, width=20).grid(row=14)

    def add_file(self):

        self.button_add = ttk.Button(
            self.root, text='Ajoutée l\'image svg', command=self.__add_file, width=20).grid(row=14, column=3)

    def __add_file(self):
        file = filedialog.askopenfile(
            title='Ajoutée un fichier svg',
            initialdir=str(Path.home()),
            filetypes=self.filetype
        )

        messagebox.showinfo(title='Seléctionnée un fichier', message=file)

    def preview(self):

        self.button_preview = ttk.Button(
            self.root, text="Prévisualisée", width=20).grid(row=14, column=1)

    def error(self, title: str, message: str):

        messagebox.showerror(title, message)

    def validate_information(self):

        messagebox.showinfo('Validée', 'La validation a bien été effectuée')
