import tkinter as tk
from tkinter import ttk

from models import Animal

# Créer la fenêtre principale
root = tk.Tk()
root.geometry("1200x800")
root.title("Veto-2000")


# Créer un Treeview
tree = ttk.Treeview(
    root,
    columns=("Nom", "Espèce", "Date de naissance", "Couleur", "Poids"),
    show="headings",
)
tree.geometry("1000x600")
tree.heading("Nom", text="Nom")
tree.heading("Espèce", text="Espèce")
tree.heading("Date de naissance", text="Date de naissance")
tree.heading("Couleur", text="Couleur")
tree.heading("Poids", text="Poids")

# Ajouter des données au Treeview
tree.insert("", "end", values=("Rex", "Chien", "01/01/2015", "Marron", "25kg"))
tree.insert("", "end", values=("Mimi", "Chat", "15/03/2018", "Noir", "4kg"))

tree.pack(pady=20)

# Lancer la boucle principale
root.mainloop()
