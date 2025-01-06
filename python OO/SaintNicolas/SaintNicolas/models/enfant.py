from models.comportement import Comportement
from models.personne import Personne

class Enfant (Personne):
    def __init__(self, nom: str, age: int, comportement: Comportement):
        super().__init__(nom, age)        
        self.comportement = comportement

    @property
    def comportement(self):
        return self.__comportement
    
    @comportement.setter
    def comportement(self, value):
        if (not isinstance(value, Comportement)):
            raise TypeError("Le comportement doit être Gentil, Moyen, Mechant")
        self.__comportement = value

    def __str__(self):
        return f"L'enfant ({self.nom} est âgé de {self.age} ans(s) et a été {self.comportement.value} cette année)"

    def est_eligible(self):
        return self.comportement in (Comportement.GENTIL, Comportement.MOYEN)
