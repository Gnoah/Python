# -*- coding: Latin-1 -*- 
from tkinter import * 
from math import *
 
 
#Fonction calcul 
def calcul (): 
    #Récupération des variables
    chaine.configure(text = "Soit une équation de la forme : ax^2 + bx + c = 0")
    a=int(A.get()) 
    b=float(B.get()) 
    c=float(C.get()) 
 
    #Calcul 
    delta = b**2 - 4*a*c
    chaine1.configure(text = delta)

    if (delta < 0):
        chaine2.configure(text = "L'équation n'a pas de solution")
    else:
        if a == 0:
            chaine3.configure(text = 'a = 0')
            chaine4.configure(text = "L'équation est premier degrer")
            x = -c / b
            chaine5.configure(text = "donc x = {}".format(x))
        elif (delta == 0):
            chaine3.configure(text = "L'équation a une solution double.")
            x = -b / (2.*a)
            chaine4.configure(text = "La solution est x = {}".format(x))
        
        else:
            chaine.configure(text = "L'équation a deux solutions solutions.")
            x1 = (-b - math.sqrt(delta)) /(2*a)
            x2 = (-b + math.sqrt(delta)) /(2*a)
            chaine5.configure(text = "Les solutions sont x1 = {}".format(x1))
            chaine6.configure(text = "Les solutions sont x2 = {}".format(x2))

fenetre = Tk()
fenetre.title("Calcule seconde degrer") 
 
txt1=Label(fenetre, text="A:").grid(row=2, column=2) 
txt2=Label(fenetre, text='B:').grid(row=3, column=2) 
txt3=Label(fenetre, text='C:').grid(row=4, column=2)
Button(fenetre,text='Calculer',command=calcul).grid(row=5 , column=2) 
Button(fenetre,text='Quitter',command=fenetre.destroy).grid(row=5, column=4) 
 
A=Entry(fenetre) 
B=Entry(fenetre) 
C=Entry(fenetre)
chaine = Label(fenetre)
chaine1 = Label(fenetre) 
chaine2 = Label(fenetre) 
chaine3 = Label(fenetre) 
chaine4 = Label(fenetre)
chaine5 = Label(fenetre)
chaine6 = Label(fenetre)
 
A.grid(row=2, column=3) 
B.grid(row=3, column=3) 
C.grid(row=4, column=3)
chaine.grid(row=1, column=2)
chaine1.grid(row=6, column=2) 
chaine2.grid(row=7, column=2) 
chaine3.grid(row=8, column=2)
chaine4.grid(row=9, column=2)
chaine5.grid(row=10, column=2)
chaine6.grid(row=11, column=2) 
 
fenetre.mainloop()

# import tkinter as tk
 
 
# def calculate(ev=None):
#     get_values = lambda: (float(entry.get() or 0) for entry in entries)
#     a, b, c = get_values()
#     try:
#         label["text"] = "Delta = {}".format((
#             b**2 - 4*a*c
#         ))
#     except ZeroDivisionError:
#         label["text"] = "Delta = 0"
 
# def is_float(value):
#     try:
#         float(value or 0)
#     except (ValueError, OverflowError):
#         return False
#     return True
 
 
# frame = tk.Frame()
# frame.pack()
 
# vcmd = frame.register(is_float)
 
# entries = []
# for index, text in enumerate(("a:", "b:", "c:")):
#     row, col = divmod(index, 2)
#     col *= 2
#     tk.Label(frame, text=text).grid(row=row, column=col)
#     entry = tk.Entry(frame, validate="all", validatecommand=(vcmd, "%P"))
#     entry.grid(row=row, column=col + 1)
#     entry.bind("<KeyRelease>", calculate)
#     entries.append(entry)
 
# row, col = divmod(index + 1, 2)
# col *= 2
# label = tk.Label(frame, text="Delta = 0")
# label.grid(row=row, column=col, columnspan=2)
 
# frame.mainloop()

import math

print("Soit une équation de la forme : ax^2 + bx + c = 0")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b**2 - 4*a*c
print('Delta égale =',delta)

if(delta < 0):
    print("L'équation n'a pas de solution")
else:
    if a == 0:
        print('a = 0')
        print("L'équation est premier degrer")
        x = -c / b
        print ("donc X = ",x)
    elif (delta == 0):
        print("L'équation a une solution double.")
        x = -b / (2.*a)
        print ("La solution est x = ",x)
    
    else:
        print("L'équation a deux solutions solutions.")
        x1 = (-b - math.sqrt(delta)) /(2*a)
        x2 = (-b + math.sqrt(delta)) /(2*a)
        print ("Les solutions sont x1 = ",x1, " et ", x2)
