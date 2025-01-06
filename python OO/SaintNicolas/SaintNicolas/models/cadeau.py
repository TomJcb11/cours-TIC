from abc import ABC, abstractmethod

class Cadeau (ABC):
    def __init__(self, nom: str, valeur: int, stock: int):
        super().__init__()
        self.__nom = nom
        self.valeur = valeur       
        self.stock = stock
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def valeur(self):
        return self.__valeur

    @valeur.setter
    def valeur(self, value:int): 
        if(not isinstance(value,int)):
            raise TypeError("la valeur du cadeau doit être numérique")
        if(value is None or value < 1 or value > 10):
            raise ValueError("La valeur du cadeaux doit être compris entre 1 et 10")
        else:
            self.__valeur = value

    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, value):
        if(not isinstance(value,int)):
            raise TypeError("la valeur du stock doit être numérique")
        if (value < 0):
            raise ValueError("La valeur doit être positive")
        self.__stock = value
    
    
    @abstractmethod
    def enlever_du_stock(self, quantite:int):
        pass
        
    def __str__(self):
        return f"Le cadeau {self.nom} d'une qualité de {self.valeur} étoile(s) est en stock : {self.stock}" 