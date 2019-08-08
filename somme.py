import tkinter as tk
 
def calcul_somme(event):
    somme = varA.get() + varB.get()
    resultat.set(somme)
 
 
fenetre = tk.Tk()
 
## FRAME (Contenant un label et le résultat):
frame = tk.Frame(fenetre)
frame.pack()
# label
 
resultat = tk.IntVar()
lbl_resultat = tk.Label(frame, textvariable=resultat)
lbl_resultat.pack()
 
## Tous les entries.
varA = tk.IntVar()
varB = tk.IntVar()
 
entryA = tk.Entry(fenetre, textvariable=varA)
entryA.bind('<KeyRelease>', calcul_somme)
entryA.pack()
 
entryB = tk.Entry(fenetre, textvariable=varB)
entryB.bind('<KeyRelease>', calcul_somme)
entryB.pack()
 
 
fenetre.mainloop()

print("Somme de deux nombre : a + b ")

a = float(input("a = "))
b = float(input("b = "))

somme = a + b
print("somme =",somme)