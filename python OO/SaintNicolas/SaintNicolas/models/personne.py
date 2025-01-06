from abc import ABC, abstractmethod

class Personne (ABC):
    
    def __init__(self, nom, age):
        super().__init__()
        self.__nom = nom
        if(not isinstance(age,int)):
            raise TypeError("l'âge doit être numérique")
        self.age = age
    
    @property
    def nom(self):  
        return self.__nom
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if(not isinstance(value,int)):
            raise TypeError("l'âge doit être numérique")
        if(value<=0 or value>14):
          raise ValueError("L'enfant doit être âgé de plus de 0 ans et de moins de 15 ans")
        self.__age = value
        
    @abstractmethod
    def est_eligible():
        pass