import time
from models.elephant import Elephant
from models.python import Python
from models.girafe import Girafe
from models.lion import Lion


class Enclos:
    def __init__(self, nom, capacite_max, taille, liste_animaux=[]):
        self._nom = nom
        self._capacite_max = capacite_max
        self._taille = taille
        self._liste_animaux = liste_animaux

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def capacite_max(self):
        return self._capacite_max

    @capacite_max.setter
    def capacite_max(self, value):
        self._capacite_max = value

    @property
    def taille(self):
        return self._taille

    @property
    def liste_animaux(self):
        return self._liste_animaux

    def ajouter_animal(self, animal):
        if animal in self.liste_animaux:
            print(f"{animal.nom} se trouve déjà dans l'enclos ❌")
        elif len(self.liste_animaux) >= self.capacite_max:
            print("L'enclos est plein, impossible d'ajouter un nouvel animal ❌")
        else:
            self.liste_animaux.append(animal)
            print(f"{animal.nom} ajouté à l'enclos ✅")

    def enlever_animal(self, animal):
        if animal in self.liste_animaux:
            self.liste_animaux.remove(animal)
            print(f"- {animal.nom} retiré de l'enclos , à la poubelle 👋")
        else:
            print(f"- {animal.nom} n'est pas présent dans l'enclos ❌")

    def afficher_animaux(self):
        if self.liste_animaux:
            print("Animaux dans l'enclos :")
            for animal in self.liste_animaux:
                if animal.en_vie:
                    print("--------------------------")
                    print(f"Nom             : {animal.nom}")
                    print(f"Satisfaction    : {animal.bonheur} / 100")
                    print(f"Appétit         : {animal.rassasier} / 100")
                    print(f"Régime alimentaire : {animal.regime_alimentaire}")
                    if isinstance(animal, Elephant):
                        print(f"Taille oreilles : {animal.taille_oreilles}")
                        print(f"Longueur défense : {animal.longueur_defense}")
                    elif isinstance(animal, Girafe):
                        print(f"Longueur du cou : {animal.longueur_du_cou}")
                    elif isinstance(animal, Python):
                        print(f"Longueur        : {animal.longueur}")
                    elif isinstance(animal, Lion):
                        print(f"Prédation       : {animal.predation}")

                    print("--------------------------")
                else:
                    print("--------------------------")
                    print(f"💀 {animal.nom} est mort 💀")
                    print("--------------------------")
        else:
            print("--------------------------")
            print("L'enclos est vide...")
            print("--------------------------")

    def passer_un_jour(self):
        print("Passage d'une journée... 🌞")
        time.sleep(2)
        print("Les résidents s'occupents comme ils peuvent : \n")
        for animal in self.liste_animaux:
            if self.liste_animaux == []:
                print("Game over")
                return
            # si on a plus d'animaux dans l'enclos on arrête le programme et on affiche game over:
            animal.diminuer_rassasier()
            animal.diminuer_bonheur()
            animal.observer_environnement()

            if not animal.en_vie:
                self.enlever_animal(animal)
                time.sleep(2)
        self.afficher_animaux()

        print("Journée terminée 🌙")
        time.sleep(1)
