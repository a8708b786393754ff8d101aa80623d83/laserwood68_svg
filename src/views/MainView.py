import tkinter as ttk


class MainView(ttk.Frame):
    def __init__(self, root: ttk.Tk):
        super().__init__()
        self.number_ = ttk.StringVar()
        self.title_ = ttk.StringVar()

        self.root = root

    def number(self):
        self.label_number = ttk.Label(
            self.root, text='Numero du personnage: ').grid(row=0)
        self.entry_number = ttk.Entry(
            self.root, textvariable=self.number_).grid(row=0, column=1)

    def title(self):
        self.label_title = ttk.Label(self.root, text='Titre', width=20).grid(row=1)
        self.entry_title = ttk.Entry(self.root, textvariable=self.title_).grid(row=1, column=1)

    def validate(self):
        self.button_validate = ttk.Button(self.root, text='Validée').grid()
        
        
    def pre_vizuialisation(self): 
        self.button_pre_visual = ttk.Button(self.root, texte="Pre-Visualiser").grid()
