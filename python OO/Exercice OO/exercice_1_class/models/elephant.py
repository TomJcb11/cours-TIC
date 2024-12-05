import random
from models.animal import Animal


class Elephant(Animal):
    def __init__(
        self,
        nom="",
        soigneur=None,
        taille_oreilles=105,
        longueur_defense=90,
        regime_alimentaire="Herbivore",
    ):
        super().__init__(
            nom=nom, soigneur=soigneur, regime_alimentaire=regime_alimentaire
        )
        self.taille_oreilles = taille_oreilles
        self.longueur_defense = longueur_defense

    def afficher_info(self):
        super().afficher_info()
        print(
            f"- Taille des oreilles: {self.taille_oreilles} cm \n longueur des défense: {self.longueur_defense} cm"
        )

    def prendre_bain_boue(self):
        if self.en_vie:
            print(f"- {self.nom} prend un bain de boue 🐘 ")
            self.bonheur += 5
            self.rassasier += 20

    def aspirer_eau(self):
        if self.en_vie:
            print(f"{self.nom} aspire l'eau et recrache tout sur les visiteurs.")
            self.bonheur += 20

    def casser_defense(self):
        if self.en_vie:
            print(
                f"{self.nom} à trop le seum parcequ'il a cassé une défense en jouant avec un arbre, mais quel con lui aussi ! "
            )
            self.bonheur -= 30
            self.longueur_defense = 10

    def observer_environnement(self):
        random_action = random.randint(1, 20)
        augmentation_defense = random.randint(5, 15)
        self.longueur_defense += augmentation_defense
        print(
            f"- {self.nom} regarde les visiteurs et les enfants qui lui jettent des cacahuètes"
        )

        print(
            f"- La longueur des défense de {self.nom} à encore augmenté aujourd'hui de {augmentation_defense} cm et on maintenant une longeur de {self.longueur_defense} cm"
        )
        if random_action <= 5:
            self.prendre_bain_boue()
            self.bonheur += 5
        elif random_action <= 10:
            self.aspirer_eau()
            self.bonheur += 25
        elif random_action >= 18:
            self.casser_defense()

        return super().observer_environnement()
