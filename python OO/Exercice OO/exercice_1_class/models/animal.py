import random
from models.soigneur import Soigneur


class Animal:
    def __init__(
        self,
        nom,
        rassasier=100,
        bonheur=100,
        soigneur=None,
        regime_alimentaire="Herbivore",
    ):
        self.nom = nom
        self.soigneur = soigneur if soigneur else Soigneur()
        self.__rassasier = rassasier if rassasier else 100
        self.__bonheur = bonheur if bonheur else 100
        self.__en_vie = True
        self.__regime_alimentaire = regime_alimentaire

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def rassasier(self):
        return self.__rassasier

    @rassasier.setter
    def rassasier(self, value):
        self.__rassasier = value

    @property
    def bonheur(self):
        return self.__bonheur

    @bonheur.setter
    def bonheur(self, value):
        self.__bonheur = value

    @property
    def en_vie(self):
        return self.__en_vie

    @en_vie.setter
    def en_vie(self, value):
        self.__en_vie = value

    @property
    def soigneur(self):
        return self.__soigneur

    @soigneur.setter
    def soigneur(self, value):
        self.__soigneur = value

    @property
    def regime_alimentaire(self):
        return self.__regime_alimentaire

    def manger(self, nom_soigneur):
        if nom_soigneur == self.soigneur.nom:
            self.__rassasier = 100
            self.__bonheur += random.randint(10, 20)
            return True
        else:
            print(f"Le soigneur {nom_soigneur} n'est pas autorisé à nourrir {self.nom}")

    def _definir_satiete(self, level):
        if level >= 0 and level <= 100:
            self.__rassasier = level
        else:
            print("Le taux de satieté doit être entre 0 et 100")

    def diminuer_rassasier(self):
        level = self.__rassasier - random.randint(10, 30)
        self._definir_satiete(level)
        if self.__rassasier <= 0:
            self.__en_vie = False
            self.__rassasier = 0
            self.__bonheur = 0
            print(f"- {self.nom} est mort de faim ☠️")
        elif self.__rassasier <= 40:
            self.manger(self.soigneur.nom)

    def diminuer_bonheur(self):
        self.__bonheur -= random.randint(10, 20)
        if self.__bonheur <= 0:
            self.__bonheur = 0
            self.__en_vie = False
            print(f"- {self.nom} est mort de chagrin mskn ☠️")

    def observer_environnement(self):
        if self.__en_vie:
            print(f"- {self.nom} a fini de jouer et retourne se coucher 😴 \n")
