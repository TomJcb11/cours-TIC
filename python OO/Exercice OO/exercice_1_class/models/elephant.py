import random
from models.soigneur import Soigneur


class Elephant:
    def __init__(self, nom="", soigneur=None):
        self._nom = nom
        self._rassasier = 100
        self._bonheur = 100
        self._en_vie = True
        self._soigneur = soigneur if soigneur else Soigneur()

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def rassasier(self):
        return self._rassasier

    @property
    def bonheur(self):
        return self._bonheur

    @property
    def en_vie(self):
        return self._en_vie

    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, value):
        self._soigneur = value

    def manger(self, nom_soigneur):
        if nom_soigneur == self._soigneur.nom:
            self._rassasier = 100
            return True
        else:
            print(f"Le soigneur {nom_soigneur} n'est pas autorisé à nourrir {self.nom}")

    def diminuer_rassasier(self):
        self._rassasier -= random.randint(10, 30)
        if self._rassasier <= 0:
            self._en_vie = False
            self._rassasier = 0
            self._bonheur = 0
            print(f"{self.nom} est mort de faim ☠️")

    def diminuer_bonheur(self):
        self._bonheur -= random.randint(10, 20)
        if self._bonheur <= 0:
            self._bonheur = 0
