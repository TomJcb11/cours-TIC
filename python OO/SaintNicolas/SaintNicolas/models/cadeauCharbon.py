import random
from models.cadeau import Cadeau

class CadeauCharbon(Cadeau):
    
    def __init__(self,  valeur, quantite_dispo):
        super().__init__('Charbon', valeur, stock=quantite_dispo)
    
    def __str__(self):
        return f"{super().__str__()}"
    
    @Cadeau.valeur.setter
    def valeur(self, value:int): 
        if(not isinstance(value,int)):
            raise TypeError("la valeur du cadeau doit être numérique")
        if(value is None or value < 0 or value > 3):
            raise ValueError("La valeur du cadeaux doit être compris entre 0 et 3")
        else:
            Cadeau.valeur.fset(self, value)
    
    def enlever_du_stock(self, quantite):
        if(quantite <= self.stock):
            self.stock -= quantite
        else:
            raise ValueError("Il n'y a pas assez de charbon en stock")
