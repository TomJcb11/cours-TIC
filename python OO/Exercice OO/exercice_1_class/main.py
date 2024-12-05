import os
import time
from datetime import datetime

from models.elephant import Elephant
from models.python import Python
from models.girafe import Girafe
from models.lion import Lion

from models.enclos import Enclos
from models.soigneur import Soigneur


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    # region Encodage
    clear_console()
    print("Simulation de vie au sein d'un enclos 😃")
    time.sleep(3)
    clear_console()

    """
    # Infos soigneur
    print("Veuillez saisir les informations demandées pour le soigneur :\n")
    soigneur_nom = input("Nom du soigneur : ")
    date_naissance_str = input("Date de naissance (format YYYY-MM-DD) : ")
    try:
        date_naissance = datetime.strptime(date_naissance_str, "%Y-%m-%d").date()
        print(
            f"Date de naissance valide : {date_naissance}. Vous avez donc {datetime.now().year - date_naissance.year} ans."
        )
    except ValueError:
        print("Date invalide. Par défaut, la date sera aujourd'hui.")
        date_naissance = datetime.now().date()

    experience = int(input("Années d'expérience : "))
    soigneur = Soigneur(
        nom=soigneur_nom, date_naissance=date_naissance_str, experience=experience
    )
    clear_console()
    print(f"Le soigneur {soigneur.nom} a été enregistré.")
    time.sleep(2)
    """
    soigneur = Soigneur(nom="soigneur1", date_naissance="1990-01-01", experience=5)

    # Infos enclos
    """
    print("Veuillez à présent saisir les informations liées à l'enclos :\n")
    enclos_nom = input("Nom de l'enclos : ")
    capacite_max = int(input("Capacité maximale de l'enclos : "))
    taille = int(input("Taille de l'enclos (en m²) : "))
    enclos = Enclos(nom=enclos_nom, capacite_max=capacite_max, taille=taille)
    """
    enclos = Enclos(nom="enclos1", capacite_max=4, taille=400)
    clear_console()

    # Infos éléphants
    nombre_animaux = int(
        input(
            f"De combien d'animaux l'enclos sera-t-il constitué ? (max = {enclos.capacite_max}) : "
        )
    )
    clear_console()

    for i in range(nombre_animaux):
        type_animal = input(
            f"Type de l'animal #{i + 1} (1 Éléphant, 2 Python, 3 Girafe, 4 Lion) : "
        ).lower()
        if type_animal == "1":
            print("ajout d'un elephant à l'enclos.")
            nom_animal = input(f"Nom de l'animal #{i + 1} : ")
            animal = Elephant(nom=nom_animal, soigneur=soigneur, taille_oreilles=254)
        elif type_animal == "2":
            print("ajout d'un python à l'enclos.")
            nom_animal = input(f"Nom de l'animal #{i + 1} : ")
            animal = Python(nom=nom_animal, soigneur=soigneur, longueur=300)
        elif type_animal == "3":
            print("ajout d'une girafe à l'enclos.")
            nom_animal = input(f"Nom de l'animal #{i + 1} : ")
            animal = Girafe(nom=nom_animal, soigneur=soigneur, longueur_du_cou=500)
        elif type_animal == "4":
            print("ajout d'un lion à l'enclos.")
            nom_animal = input(f"Nom de l'animal #{i + 1} : ")
            animal = Lion(nom=nom_animal, soigneur=soigneur, predation=50)
        else:
            print("Type d'animal inconnu. Veuillez réessayer.")
            continue
        enclos.ajouter_animal(animal)
        time.sleep(1)
        clear_console()

    nombre_jours = int(input("Nombre de jours à simuler : "))
    clear_console()
    # endregion
    # region Simulation
    # Simulation des jours
    for jour in range(nombre_jours):
        print(f"Jour {jour + 1} :")
        if enclos.liste_animaux == []:
            print("Il n'y a plus d'animaux dans l'enclos fin de la simulation.")
            exit()

        enclos.passer_un_jour()
        print(f"Fin du jour {jour + 1}")
        time.sleep(2)
        input("Appuyez sur Entrée pour passer au jour suivant...")
        print("\n\n")

    print("Simulation terminée.")
    # endregion
