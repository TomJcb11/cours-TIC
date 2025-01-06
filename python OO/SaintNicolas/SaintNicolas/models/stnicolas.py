from models.comportement import Comportement
from models.enfant import Enfant
from models.cadeau import Cadeau

from models.utilitaire import Utilitaire

class SaintNicolas:
    def __init__(self):
        self.liste_cadeaux: list[Cadeau] = []
        self.enfants: list[Enfant] = []

    def ajouter_cadeau(self, cadeau):
        if (not isinstance(cadeau, Cadeau)):
            raise TypeError("Vous devez fournir un cadeau.")
        self.liste_cadeaux.append(cadeau)

    def ajouter_enfant(self, enfant):
        if (not isinstance(enfant, Enfant)):
            raise TypeError("Vous devez fournir un enfant.")
        self.enfants.append(enfant)

    def distribuer_cadeaux(self):
        
        cadeaux_distribues = {enfant: [] for enfant in self.enfants}

        # Trier les cadeaux par valeur décroissante
        cadeaux_tries = sorted(self.liste_cadeaux, key=lambda c: c.valeur, reverse=True)

        # Distribuer les cadeaux aux enfants gentils en priorité
        for enfant in self.enfants:
            if enfant.comportement == Comportement.GENTIL:
                for cadeau in cadeaux_tries:
                    if Utilitaire.verifier_stock(cadeau.stock) and len(cadeaux_distribues[enfant]) < 2:
                        cadeau.enlever_du_stock(1)
                        cadeaux_distribues[enfant].append(cadeau.nom)

        # Distribuer les cadeaux restants aux enfants moyens
        for enfant in self.enfants:
            if enfant.comportement == Comportement.MOYEN:
                for cadeau in self.liste_cadeaux:
                    if Utilitaire.verifier_stock(cadeau.stock) and len(cadeaux_distribues[enfant]) < 2:
                        cadeau.enlever_du_stock(1)
                        cadeaux_distribues[enfant].append(cadeau.nom)
           
        # Distribuer les cadeaux avec valeur inférieure à 3 aux enfants méchants
        for enfant in self.enfants:
            if enfant.comportement == Comportement.MECHANT:
                for cadeau in self.liste_cadeaux:
                    if Utilitaire.verifier_stock(cadeau.stock) and cadeau.valeur < 3 and len(cadeaux_distribues[enfant]) < 1:
                        cadeau.enlever_du_stock(1)
                        cadeaux_distribues[enfant].append(cadeau.nom)

        # Afficher la distribution des cadeaux
        print("Distribution des cadeaux :")
        for enfant, cadeaux in cadeaux_distribues.items():
            if cadeaux:
                print(f"- {enfant.nom} ({enfant.comportement}) : {', '.join(cadeaux)}")
            else:
                print(f"- {enfant.nom} ({enfant.comportement}) : Aucun cadeau")

    def afficher_stock(self):
        print("Stock restant :")
        for cadeau in self.liste_cadeaux:
            print(f"- {cadeau.nom} : {cadeau.stock}")