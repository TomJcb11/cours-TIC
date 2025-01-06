# Exercices Recaps

## **Calculatrice Avancée**

* Crée une classe `Calculatrice` qui :
  * Permet d’effectuer les opérations de base (`addition`, `soustraction`, `multiplication`, `division`).
  * Contient une méthode `historique` pour garder en mémoire les 10 dernières opérations.
* Ajoute une méthode `evaluer_expression(expression)` qui prend une expression mathématique sous forme de chaîne (ex. `"3 + 5 * 2"`) et renvoie le résultat en utilisant `eval`.
* Teste avec plusieurs calculs.

## **Gestionnaire de Tâches avec Priorités**

* Crée une classe `Tache` avec :
  * Les attributs `nom`, `description`, et `priorite` (1 = urgente, 5 = faible).
* Crée une classe `GestionnaireDeTaches` qui :
  * Stocke une liste de tâches.
  * Permet d’ajouter, supprimer et afficher les tâches triées par priorité.
  * Contient une méthode `executer_prochaine()` qui supprime et retourne la tâche avec la priorité la plus élevée.
* Simule l'ajout et l'exécution de plusieurs tâches.

## **Jeu de Cartes : Pierre Feuille Ciseau**

## **Gestionnaire de Fichiers JSON**

* Crée une classe `GestionnaireJSON` qui :
  * Charge un fichier JSON (fichier de données au choix).
  * Contient une méthode `rechercher(cle, valeur)` pour trouver tous les objets correspondant à une paire clé-valeur dans les données.
  * Contient une méthode `ajouter_entree(entree)` pour ajouter une entrée aux données et sauvegarder dans le fichier.
* Teste avec un fichier JSON contenant des informations simples (ex. une liste de livres, films, ou contacts).

## **Création d’un Labyrinthe**

* Crée une classe `Labyrinthe` qui :
  * Génère un labyrinthe sous forme de grille (tableau 2D).
  * Contient une méthode `afficher_labyrinthe()` pour afficher la grille.
  * Implémente un algorithme de recherche de chemin (`DFS` ou `BFS`) pour trouver un chemin de l’entrée à la sortie.
* Crée une classe `Joueur` qui peut se déplacer dans le labyrinthe en suivant un chemin valide.
