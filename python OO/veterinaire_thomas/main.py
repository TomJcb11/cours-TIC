import models.class_animal as ca

from datetime import datetime

texte = "Bonjour et bienvenue chez Veto-2000 la clinique vetérinaire du futur, ici vous pouvez \n - déposer votre animal pour une consultation (d) \n - vacciner votre animal (v) \n - retirer votre animal après consultation (r) \n - voir la liste des animaux présents (l) \n - quitter l'application (q)\n Que voulez-vous faire ? \n"

action_available = ["d", "v", "r", "l", "q"]
known_animals = []
input_action = ""
while input_action != "q":
    input_action = input(texte)
    if input_action not in action_available:
        print("Action non reconnue, veuillez recommencer plus tard")
    elif input_action == "l":
        for animal in known_animals:
            print(
                f"nom : {animal.name}, \n espèce : {animal.species},\n date de naissance : {animal.birthdate}, \n couleur : {animal.color}, \n poids : {animal.weight}, \n vacciné : {animal.vaccine},\n"
            )
    elif input_action == "d":
        name = input("Nom de l'animal: ")
        species = input("Espèce de l'animal: ")
        birthdate = datetime.strptime(
            input("Date de naissance de l'animal (YYYY-MM-DD): "),
            "%Y-%m-%d",  # on bind la date à un format date
        )
        color = input("Couleur de l'animal: ")
        weight = input("Poids de l'animal: ")
        new_animal = ca.Animal(name, species, birthdate, color, weight)
        known_animals.append(new_animal)
        print("Animal ajouté")
    elif input_action == "v":
        name = input("Nom de l'animal à vacciner: ")
        for animal in known_animals:
            if animal.name == name:
                animal.vaccine()
    elif input_action == "r":
        name = input("Nom de l'animal à retirer: ")
        if known_animals == []:
            print("Il n'y a pas d'animaux à retirer")
            break
        for animal in known_animals:
            if animal.name == name:
                animal.return_animal()
                known_animals.remove(animal)


print("Merci de votre visite, à bientôt")
