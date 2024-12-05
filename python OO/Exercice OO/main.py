from models.elephant import Elephant
from models.soigneur import Healer

from datetime import datetime

"""
    birthdate=datetime.strptime(
        input("Date de naissance du soigneur (YYYY-MM-DD): "),
        "%Y-%m-%d",  # on bind la date à un format date
    )
"""


def a_new_animal_added_to_healer(animal, healer):
    """On peut attribuer les soins d'un animal à un soigneur en utilisant la méthode prope à chaque classe

    Args:
        animal (_type_): _description_
        healer (_type_): _description_
    """
    healer.add_animal(animal)
    animal.add_healer(healer)


"""   Création des instances de la classe Elephant   """
animal1 = Elephant()
animal2 = Elephant(name="blabla")

"""  Création des instances de la classe Healer   """

le_zozo_du_zoo = Healer(
    name="Bleu",
    birthdate="2012/12/12",
)
arracheur_de_naine = Healer(
    name="Rouge",
    birthdate="2012/12/12",
)


# a_new_animal_added_to_healer(animal1, le_zozo_du_zoo)
# a_new_animal_added_to_healer(animal1, arracheur_de_naine)

# a_new_animal_added_to_healer(animal2, le_zozo_du_zoo)
# # print(le_zozo_du_zoo.find_animal_by_healer())
# print(animal2.find_healer_by_animal())
# # print(animal1.find_healer_by_animal())
# print(le_zozo_du_zoo)


message_de_demarrage = """Bienvenue sur le programme de gestion du Zoo, veuillez choisir une option:
1. Ajouter un soigneur
2. Ajouter un animal
3. Attribuer un soigneur à un animal
4. Afficher les informations d'un soigneur
5. Afficher les informations d'un animal
6. Quitter
"""

liste_animal = []
liste_soigneur = []
input("Press Enter to start ZooKeeper... \n")
choix = True
while choix:
    action = int(input(message_de_demarrage))
    match action:
        case 1:
            name = input("Nom du soigneur: ")
            try:
                birthdate = datetime.strptime(
                    input("Date de naissance du soigneur (YYYY-MM-DD): "),
                    "%Y-%m-%d",  # on bind la date à un format date
                )
                print(
                    f"Date de naissance valide : {birthdate}, vous avez donc {datetime.now().year - birthdate.year} ans"
                )

            except ValueError:
                print(
                    "Format de date invalide. Veuillez entrer la date au format YYYY-MM-DD."
                )
            experience = int(input("Années d'expérience: "))
            animal_count = 0
            liste_soigneur.append(Healer(name, birthdate, experience, animal_count))
            print(liste_soigneur[-1])
        case 2:
            name = input("Nom de l'animal: ")
            appetite = 50
            hapiness = 50
            liste_animal.append(
                Elephant(name=name, appetite=appetite, hapiness=hapiness)
            )
            print(liste_animal[-1])
        case 3:
            animal_name = input("Nom de l'animal: ")
            healer_name = input("Nom du soigneur: ")
            for animal in liste_animal:
                if animal.name == animal_name:
                    for healer in liste_soigneur:
                        if healer.name == healer_name:
                            a_new_animal_added_to_healer(animal, healer)
                            print(f"{animal.name} a été attribué à {healer.name}")
        case 6:
            print("Au revoir")
            choix = False
