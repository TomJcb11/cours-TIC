import os
import time
from datetime import datetime

from models.elephant import Elephant
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

    # Infos soigneur
    print("Veuillez saisir les informations demandées pour le soigneur :\n")
    soigneur_nom = input("Nom du soigneur : ")
    date_naissance_str = input("Date de naissance (format YYYY-MM-DD) : ")
    try:
        date_naissance = datetime.strptime(date_naissance_str, "%Y-%m-%d").date()
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

    # Infos enclos
    print("Veuillez à présent saisir les informations liées à l'enclos :\n")
    enclos_nom = input("Nom de l'enclos : ")
    capacite_max = int(input("Capacité maximale de l'enclos : "))
    taille = int(input("Taille de l'enclos (en m²) : "))
    enclos = Enclos(nom=enclos_nom, capacite_max=capacite_max, taille=taille)
    clear_console()

    # Infos éléphants
    nombre_animaux = int(
        input(
            f"De combien d'animaux l'enclos sera-t-il constitué ? (max = {enclos.capacite_max}) : "
        )
    )
    clear_console()

    for i in range(nombre_animaux):
        nom_animal = input(f"Nom de l'animal #{i + 1} : ")
        elephant = Elephant(nom=nom_animal, soigneur=soigneur)
        enclos.ajouter_animal(elephant)
        time.sleep(1)
        clear_console()

    nombre_jours = int(input("Nombre de jours à simuler : "))
    clear_console()
    # endregion

    # Simulation des jours
    for jour in range(nombre_jours):
        print(f"Jour {jour + 1} :")
        enclos.passer_un_jour()
        time.sleep(1)
        clear_console()
        print(f"Fin du jour {jour + 1}")
        time.sleep(2)
        clear_console()

    print("Simulation terminée.")
