from models.animal import Animal


class Lion(Animal):
    def __init__(
        self, nom="", soigneur=None, predation=0, regime_alimentaire="Carnivore"
    ):
        super().__init__(
            nom=nom, soigneur=soigneur, regime_alimentaire=regime_alimentaire
        )
        self.predation = predation

    def augmenter_predation(self, augmentation):
        if self.predation >= 100:
            print(
                f"{self.nom} s'est enfui et a dévoré les visiteurs et est maintenant repu et calmé , ce sont des choses qui arrivent."
            )
            self.predation = 0
            self.bonheur = 100
            self.rassasier = 100
        else:
            self.predation += augmentation
            self.bonheur -= 10
            print(
                f"{self.nom} a augmenté sa predation de {augmentation} %, il est maintenant à {self.predation} %"
            )

    def afficher_info(self):
        super().afficher_info()
        print(f"Predation: {self.predation} %")

    def observer_environnement(self):
        self.augmenter_predation(30)
        print(
            f"- {self.nom} regarde les visiteurs et les imagine en morceaux de viande"
        )
        return super().observer_environnement()
