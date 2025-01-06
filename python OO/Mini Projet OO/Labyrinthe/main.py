from models.joueur import Joueur
from models.labyrinthe import Labyrinthe


def main():
    labyrinthe = Labyrinthe(50, 50)
    labyrinthe.afficher_labyrinthe()
    chemin = labyrinthe.trouver_chemin()
    print("Chemin trouvé :", chemin)

    joueur = Joueur(labyrinthe)
    joueur.afficher_position()

    # Déplacer le joueur selon le chemin trouvé
    for position in chemin[1:]:
        x, y = position
        if (x, y) == (joueur.position[0], joueur.position[1] - 1):
            joueur.deplacer("haut")
        elif (x, y) == (joueur.position[0], joueur.position[1] + 1):
            joueur.deplacer("bas")
        elif (x, y) == (joueur.position[0] - 1, joueur.position[1]):
            joueur.deplacer("gauche")
        elif (x, y) == (joueur.position[0] + 1, joueur.position[1]):
            joueur.deplacer("droite")
        # joueur.afficher_position()


if __name__ == "__main__":
    main()
