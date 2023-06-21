import tkinter.messagebox as messagebox


def error(title: str, message: str):

    messagebox.showerror(title, message)


def succes():
    
    messagebox.showinfo('Validée', 'La validation a bien été effectuée')
