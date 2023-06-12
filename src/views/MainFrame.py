import tkinter as ttk


class MainFrame(ttk.Frame):
    def __init__(self, root: ttk.Tk):
        super().__init__()
        self.numbers_ = ttk.StringVar()
        self.title_ = ttk.StringVar()

        self.root = root

    def number(self):
        self.label_number = ttk.Label(
            self.root, text='Numero du personnage: ').grid(row=0)
        self.listbox = ttk.Entry(self.root, textvariable=self.numbers_).grid(row=0, column=1)

    def title(self):
        self.label_title = ttk.Label(
            self.root, text='Titre', width=20).grid(row=1)
        self.entry_title = ttk.Entry(
            self.root, textvariable=self.title_).grid(row=1, column=1)

    def validate(self):
        self.button_validate = ttk.Button(self.root, text='Validée').grid()

    def preview(self):
        self.button_preview = ttk.Button(
            self.root, text="Prévisualisée").grid()