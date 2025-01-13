# Correction extraction simple

#### Exo 1
Donner les styles de cuisine présents dans la collection
```js
db.getCollection("restaurants").distinct("cuisine");
```

#### Exo 2
Donner tous les grades possibles dans la base
```js
db.getCollection("restaurants").distinct("grades.grade")
```

#### Exo 3
Compter le nombre de restaurants proposant de la cuisine française ("French")
```js
db.getCollection("restaurants").countDocuments({"cuisine": "French"})
```
### Exo 4
Compter le nombre de restaurants situé sur la rue "Central Avenue"
````js
db.getCollection("restaurants").countDocuments({"address.street": "Central Avenue"})
````

### Exo 5
Compter le nombre de restaurants ayant eu une note supérieure à 50
````js
db.getCollection("restaurants").countDocuments({"grades.score": {$gt: 50}})
````

### Exo 6
Lister tous les restaurants, en n'affichant que le nom, l'immeuble et la rue
````js
db.getCollection("restaurants").find({}, {"name": true, "address": {"building": true, "street": true}});
````
### Exo 7
Lister tous les restaurants nommés "Burger King" (nom et quartier uniquement)
````js
db.getCollection("restaurants").find({"name": "Burger King"}, {"name": true, "borough": true});
````
### Exo 8
Lister les restaurants situés sur les rues "Union Street" ou "Union Square"
````js
db.getCollection("restaurants").find({"address.street": {$in: ["Union Street", "Union Square"]}});
````

### Exo 9
Lister les restaurants situés au-dessus de la latitude 40.90
````js
db.getCollection("restaurants").find({"address.coord.1": {$gt: 40.9}})
````
### Exo 10
Lister les restaurants ayant eu un score de 0 et un grade "A"
````js
db.getCollection("restaurants").find({"address.coord.1": {$gt: 40.9}})
````