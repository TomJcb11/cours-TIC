from models.comportement import Comportement


class Utilitaire:
    
    @staticmethod
    def verifier_age(age: int) -> bool:
        return age > 0
    
    @staticmethod
    def verifier_comportement(comportement: Comportement) -> bool:
        return comportement in Comportement
    
    @staticmethod
    def verifier_valeur(valeur: int) -> bool:
        return 1 <= valeur <= 10
    
    @staticmethod
    def verifier_qualite(valeur: int,comportement: Comportement) -> bool:
        if comportement == Comportement.GENTIL and 7 <= valeur <= 10: return True
        elif comportement == Comportement.MOYEN and 3 <= valeur <= 6: return True
        elif comportement == Comportement.MECHANT and 0 <= valeur <= 3: return True
        
        return False
    
    @staticmethod
    def verifier_stock(stock): 
        return stock > 0