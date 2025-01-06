import random
from models.cadeau import Cadeau

class CadeauMagique(Cadeau):
    

    def __init__(self, nom,  valeur, quantite_dispo):
        super().__init__(nom, valeur, stock=quantite_dispo)
        self.__magique = True;
        self.__magical_effects = [
          "S'adapte à la température exacte et protège contre les cauchemars",
          "Change de couleur selon l'humeur de l'enfant",
          "Transforme les dessins en mondes miniatures explorables",
          "Enregistre et rejoue des moments spéciaux de la vie de l'enfant",
          "Permet de marcher sur différentes surfaces impossibles",
          "Se transforme en bouclier protecteur invisible",
          "Projette les rêves de l'enfant sur les murs de sa chambre",
          "Révèle temporairement des talents ou super-pouvoirs uniques" 
            ]
        self.__description_magique= self.__ajouter_effet_magique()

    def __str__(self):
        return f"{super().__str__()} - ★MAGIQUE★ - { self.__description_magique}"
    
    @Cadeau.valeur.setter
    def valeur(self, value:int): 
        if(not isinstance(value,int)):
            raise TypeError("la valeur du cadeau doit être numérique")
        if(value is None or value < 7 or value > 10):
            raise ValueError("La valeur du cadeaux doit être compris entre 7 et 10")
        else:
            Cadeau.valeur.fset(self, value)

    
    def __ajouter_effet_magique(self):
        effet = random.choice(self.__magical_effects)     
        return effet

    def enlever_du_stock(self, quantite):
        if(quantite <= self.stock):
            self.stock -= quantite
        else:
            raise ValueError("Il n'y a pas assez de cadeaux magique en stock")
