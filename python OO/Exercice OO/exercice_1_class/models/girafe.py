import random
from models.animal import Animal


class Girafe(Animal):
    def __init__(
        self, nom="", soigneur=None, longueur_du_cou=350, regime_alimentaire="Herbivore"
    ):
        super().__init__(
            nom=nom, soigneur=soigneur, regime_alimentaire=regime_alimentaire
        )
        self.longueur_du_cou = longueur_du_cou

    def afficher_info(self):
        super().afficher_animaux()
        print(f"longueur du cou {self.longueur_du_cou} cm")

    def manger_feuilles(self):
        if self.rassasier > 0:
            print(f"- {self.nom} mange des feuilles, crunch crunch")
            self.rassasier += random.randint(1, 3)
            return True
        else:
            return False

    def boire_eau(self):
        if self.rassasier > 0:
            print(f"- {self.nom} boit de l'eau , glou glou glou")
            self.rassasier += random.randint(5, 5)
            return True
        else:
            return False

    def parafoudre(self):
        print(f"- {self.nom} a été touché(e) par la foudre, est mort(e) sur le coup")
        self.en_vie = False

    def observer_environnement(self):
        print(f"- {self.nom} regarde le paysage, il est content car il a vu un oiseau")
        self.bonheur += 5
        random_choice = random.randint(1, 20)
        if random_choice <= 5:
            self.boire_eau()
            self.bonheur += 15
        elif random_choice == 15:
            self.parafoudre()
        elif random_choice >= 10:
            self.manger_feuilles()
            self.bonheur += 10

        return super().observer_environnement()
