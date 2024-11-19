### Définition d'un Itérable

En Python, un **itérable** est un objet capable de retourner ses éléments un par un, permettant ainsi de parcourir ses éléments dans une boucle. Les itérables sont des objets sur lesquels on peut utiliser une boucle `for` pour accéder à leurs éléments.

#### Caractéristiques d'un Itérable

1.**Implémente la méthode `__iter__()`** : Un objet est considéré comme itérable s'il implémente la méthode spéciale `__iter__()`, qui retourne un itérateur.

2.**Peut être parcouru** : Les itérables peuvent être parcourus en utilisant une boucle `for`, des compréhensions de liste, ou d'autres constructions qui nécessitent un itérateur.

#### Exemples d'Itérables

-**Listes** : `[1, 2, 3]`

-**Tuples** : `(1, 2, 3)`

-**Chaînes de caractères** : `"abc"`

-**Dictionnaires** : `{"a": 1, "b": 2}`

-**Ensembles** : `{1, 2, 3}`

-**Objets de type `range`** : `range(5)`

#### Exemple d'Itérable

Voici un exemple montrant comment un itérable peut être parcouru avec une boucle `for` :

```python

# Liste (itérable)

numbers = [1, 2, 3, 4, 5]


# Parcourir la liste avec une boucle for

for num in numbers:

    print(num)
```

### Itérateur

Un **itérateur** est un objet qui représente un flux de données. Il implémente les méthodes `__iter__()` et `__next__()`. La méthode `__next__()` retourne le prochain élément du flux, et lève une exception `StopIteration` lorsqu'il n'y a plus d'éléments.

#### Exemple d'Itérateur

Voici comment obtenir un itérateur à partir d'un itérable et utiliser la méthode `__next__()` :

```python
# Liste (itérable)
numbers = [1, 2, 3, 4, 5]

# Obtenir un itérateur à partir de la liste
iterator = iter(numbers)

# Utiliser l'itérateur pour accéder aux éléments
print(next(iterator))  # Affiche 1
print(next(iterator))  # Affiche 2
print(next(iterator))  # Affiche 3
```

### Conclusion

Un itérable est un objet qui peut être parcouru élément par élément, généralement en utilisant une boucle `for`. Les itérables implémentent la méthode `__iter__()`, qui retourne un itérateur. Les itérateurs, quant à eux, implémentent les méthodes `__iter__()` et `__next__()`, permettant de parcourir les éléments d'un itérable de manière séquentielle. ```
