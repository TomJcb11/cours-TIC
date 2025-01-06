class Joueur:
    def __init__(self, labyrinthe):
        self.labyrinthe = labyrinthe
        self.position = (1, 1)  # Position initiale (entrée)

    def deplacer(self, direction):
        x, y = self.position
        if direction == "haut":
            nx, ny = x, y - 1
        elif direction == "bas":
            nx, ny = x, y + 1
        elif direction == "gauche":
            nx, ny = x - 1, y
        elif direction == "droite":
            nx, ny = x + 1, y
        else:
            return False

        if self.labyrinthe.grille[ny][nx] != "#":
            self.position = (nx, ny)
            return True
        return False

    def afficher_position(self):
        print(f"Position actuelle du joueur : {self.position}")
