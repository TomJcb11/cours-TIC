# Application des valeurs "privées"

```python
class Elephant:
    def __init__(self, nom="", soigneur=None):
        self._nom = nom
        self._rassasier = 100
        self._bonheur = 100
        self._en_vie = True
        self._soigneur = soigneur if soigneur else Soigneur()

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value
```

en gros on définit la propriété nom comme étant _\_nom_ et non pas _nom_ de cette façon on applique une convention qui veut dire , tu n'est pas censé y accéder directement , passe par le **_getter_**.

si on souhaite pouvoir modifier dans l'avenir une proprety on défini un **_setter_** _nom_ qui va modifier la valeur de _\_nom_ pour l'instance de la classe en dehors du constructeur.
