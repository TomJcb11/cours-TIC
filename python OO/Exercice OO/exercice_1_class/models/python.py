from models.animal import Animal

import random


class Python(Animal):
    def __init__(
        self, longueur, mue=3, nom="", soigneur=None, regime_alimentaire="Omnivore"
    ):
        super().__init__(
            nom=nom, soigneur=soigneur, regime_alimentaire=regime_alimentaire
        )
        self.longueur = longueur
        self.mue = mue

    def afficher_info(self):
        super().afficher_info()
        print(f"Longueur: {self.longueur}")

    def preparer_mue(self):
        if self.en_vie:
            if self.mue <= 0:
                print(
                    f"{self.nom} réalise sa mue , il se sent bien dans cette nouvelle peau 🐍"
                )
                self.bonheur += 50
            else:
                self.mue -= 1

    def observer_environnement(self):
        random_value = random.randint(1, 60)
        if random_value <= 10:
            print(f"- {self.nom} a l'air agité et chasse les visiteurs 🐍")
            self.bonheur -= 2
            return True
        elif random_value <= 30:
            self.preparer_mue()
            self.bonheur += 50

            return True
        elif random_value <= 50:
            print(f"- {self.nom} a mordu un visiteur 😈, fallait le laisser tranquille")
            self.bonheur -= 20
        return super().observer_environnement()
