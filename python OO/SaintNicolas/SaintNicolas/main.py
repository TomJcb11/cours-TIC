import os

from models.cadeauCharbon import CadeauCharbon
from models.cadeauMagique import CadeauMagique
from models.cadeauNormal import CadeauNormal
from models.comportement import Comportement
from models.enfant import Enfant
from models.stnicolas import SaintNicolas
from models.utilitaire import Utilitaire


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    clear_console()
    print("La grande distribution de St Nicolas - Père Noël - La befana - ...")

    try:
        # Création des cadeaux
        nintendo = CadeauNormal("Nintendo Switch", 5, 5)
        print(nintendo)
        ours = CadeauMagique("Ours", 9, 3)
        print(ours)
        livre = CadeauMagique("Livre magique", 10, 2)
        print(livre)
        chocolat = CadeauNormal("Chocolat", 5, 10)
        print(chocolat)
        charbon = CadeauCharbon(2, 5)

        ##Erreur de création de cadeau
        # troisieme_cadeau = Cadeau("Train électrique",15,2)
        # print(troisieme_cadeau)
        # Création des enfants
        alice = Enfant("Alice", 8, Comportement.GENTIL)
        print(alice)
        mike = Enfant("Mike", 11, Comportement.MOYEN)
        print(mike)
        charlie = Enfant("Charlie", 10, Comportement.MECHANT)
        print(charlie)
        diane = Enfant("Diane", 6, Comportement.GENTIL)
        print(diane)
        ## Erreur d'enumération
        # quatrieme_enfant= Enfant("Lucas",6, "MOYEN")
        # print(quatrieme_enfant)
        ## Erreur d'âge
        # troisieme_enfant= Enfant("Bernard",18, Comportement.MECHANT)
        # print(troisieme_enfant)
        # Création de st Nicolas
        st_nicolas = SaintNicolas()

        st_nicolas.ajouter_cadeau(ours)
        st_nicolas.ajouter_cadeau(nintendo)
        st_nicolas.ajouter_cadeau(livre)
        st_nicolas.ajouter_cadeau(chocolat)
        st_nicolas.ajouter_cadeau(charbon)

        st_nicolas.ajouter_enfant(alice)
        st_nicolas.ajouter_enfant(mike)
        st_nicolas.ajouter_enfant(charlie)
        st_nicolas.ajouter_enfant(diane)

        st_nicolas.distribuer_cadeaux()
        st_nicolas.afficher_stock()

    except ValueError as e:
        print(f"ERROR :{e}")
    except Exception as ex:
        print(f"EXCEPTION : Une erreur inconnue s'est produite :{ex}")
