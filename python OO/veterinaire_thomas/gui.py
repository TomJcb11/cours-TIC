import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Vétérinaire 2000")
root.geometry("1200x800")

# Create a treeview
tree = ttk.Treeview(
    root,
    columns=("Nom", "Espèce", "Date de naissance", "Couleur", "Poids", "Vacciné"),
    show="headings",
)
tree.heading("Nom", text="Nom")
tree.heading("Espèce", text="Espèce")
tree.heading("Date de naissance", text="Date de naissance")
tree.heading("Couleur", text="Couleur")
tree.heading("Poids", text="Poids")
tree.heading("Vacciné", text="Vacciné")

tree.pack(padx=10, pady=10)

root.mainloop()
