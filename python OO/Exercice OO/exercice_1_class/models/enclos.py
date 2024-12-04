import time


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
            print(f"{animal.nom} retiré de l'enclos 👋")
        else:
            print(f"{animal.nom} n'est pas présent dans l'enclos ❌")

    def afficher_animaux(self):
        if self.liste_animaux:
            print("Animaux dans l'enclos :")
            for animal in self.liste_animaux:
                if animal.en_vie:
                    print("--------------------------")
                    print(f"Nom             : {animal.nom}")
                    print(f"Satisfaction    : {animal.bonheur} / 100")
                    print(f"Appétit         : {animal.rassasier} / 100")
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
        for animal in self.liste_animaux:
            animal.diminuer_rassasier()
            animal.diminuer_bonheur()
            if not animal.en_vie:
                self.enlever_animal(animal)
                time.sleep(2)
        print("Journée terminée 🌙")
        time.sleep(1)
