import random
from models.cadeau import Cadeau

class CadeauNormal(Cadeau):
    
    def __init__(self, nom,  valeur, quantite_dispo):
        super().__init__(nom, valeur, stock=quantite_dispo)
    
    def __str__(self):
        return f"{super().__str__()}"
    
    @Cadeau.valeur.setter
    def valeur(self, value:int): 
        if(not isinstance(value,int)):
            raise TypeError("la valeur du cadeau doit être numérique")
        if(value is None or value < 3 or value > 6):
            raise ValueError("La valeur du cadeaux doit être compris entre 3 et 6")
        else:
            Cadeau.valeur.fset(self, value)
    
    def enlever_du_stock(self, quantite):
        if(quantite <= self.stock):
            self.stock -= quantite
        else:
            raise ValueError("Il n'y a pas assez de cadeaux normal en stock")
