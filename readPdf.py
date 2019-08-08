from tkinter import *
import tkinter.filedialog
from tkinter import filedialog

import tkinter as tk 
from tkinter.filedialog import askopenfilename


import webbrowser
def Ouvrir():
    filename = askopenfilename(title="Ouvrir une fichier pdf",filetypes=[('pdf files','.pdf'),('all files','.*')])
    webbrowser.open_new(filename)

# Main window
Mafenetre = Tk()
Mafenetre.title("Ouvrir pdf")

# Création d'un widget Menu
menubar = Menu(Mafenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Ouvrir un pdf",command=Ouvrir)

menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)

menubar.add_cascade(label="Aide", menu=menuaide)

# Affichage du menu
Mafenetre.config(menu=menubar)

# Création d'un widget Canvas
Canevas = Canvas(Mafenetre)
Canevas.pack(padx=5,pady=5)


# Utilisation d'un dictionnaire pour conserver une référence
gifdict={}

Mafenetre.mainloop()
