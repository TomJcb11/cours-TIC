import random


class Labyrinthe:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = self.generer_labyrinthe()

    def generer_labyrinthe(self):
        # Générer une grille vide
        grille = [[" " for _ in range(self.largeur)] for _ in range(self.hauteur)]

        # Ajouter des murs autour du labyrinthe
        for i in range(self.largeur):
            grille[0][i] = grille[self.hauteur - 1][i] = "-"
        for i in range(self.hauteur):
            grille[i][0] = grille[i][self.largeur - 1] = "|"

        # Ajouter des murs aléatoires à l'intérieur du labyrinthe
        for _ in range(int(self.largeur * self.hauteur * 0.4)):  # 20% de murs
            x, y = (
                random.randint(1, self.largeur - 2),
                random.randint(1, self.hauteur - 2),
            )
            grille[y][x] = "+"

        # Définir l'entrée et la sortie aléatoirement dans le labyrinthe
        random.shuffle([1, self.hauteur - 2])
        random.shuffle([1, self.largeur - 2])
        grille[1][1] = "E"  # Entrée
        grille[self.hauteur - 2][self.largeur - 2] = "S"  # Sortie

        return grille

    def afficher_labyrinthe(self):
        for ligne in self.grille:
            print("".join(ligne))

    def trouver_chemin(self):
        # Implémenter l'algorithme de recherche de chemin (DFS)
        start = (1, 1)
        end = (self.hauteur - 2, self.largeur - 2)
        stack = [start]
        visited = set()
        parent = {start: None}

        while stack:
            current = stack.pop()
            if current == end:
                break
            visited.add(current)
            x, y = current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < self.largeur
                    and 0 <= ny < self.hauteur
                    and self.grille[ny][nx] != "#"
                    and (nx, ny) not in visited
                ):
                    stack.append((nx, ny))
                    parent[(nx, ny)] = current

        # Reconstituer le chemin
        chemin = []
        current = end
        while current:
            chemin.append(current)
            current = parent[current]
        chemin.reverse()
        return chemin
