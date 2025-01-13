# Exercice d'agrégation

Il est bien évidemment possible de réaliser des calculs d'agrégats (de type somme, moyenne, minimum et maximum) dans MongoDB,
avec la fonction `aggregate()`. Celle-ci permet beaucoup d'autres opérations.

## Fonctions possibles

Cette fonction va prendre en paramètre un tableau nommé `pipeline` : tableau composé d'une suite d'opérations.

> Chaque opération sera faite après la précédente. L'ordre des opérations a donc une importance cruciale. Et le même opérateur
> peut apparaître plusieurs fois.

Voici quelques-unes des opérations possibles :

| Fonction         | Opération                                                                        |
| ---------------- | --------------------------------------------------------------------------------- |
| `$limit`       | restriction à un petit nombre de documents (très utiles pour tester son calcul) |
| `$sort`        | tri sur les documents                                                             |
| `$match`       | restriction sur les documents à utiliser                                         |
| `$unwind`      | séparation d'un document en plusieurs sur la base d'un tableau                   |
| `$addFields`   | ajout d'un champ dans les documents                                               |
| `$project`     | redéfinition des documents                                                       |
| `$group`       | regroupements et calculs d'agrégats                                              |
| `$sortByCount` | agrégat + tri                                                                    |
| `$lookup`      | jointure avec une autre collection                                                |
| ...              |                                                                                   |

## Syntaxe des opérations dans le `pipeline`

### `$limit`

On indique juste avec un entier le nombre de documents que l'on veut afficher.

- Limite aux 10 premiers restaurants

```js
db.restaurants.aggregate([
    { $limit: 10 }
])
```

Comme déjà vu dans le précédent TP, on peut ajouter la fonction `pretty()` au résultat pour avoir un affichage plus clair.

```js
db.restaurants.aggregate([
    { $limit: 10 }
]).pretty()
```

### `$sort`

On indique de façon identique à celle du paramètre `sort` de la fonction `find()`

- Idem avec tri sur le nom du restaurant

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $sort: { name: 1 }}
]).pretty()
```

### `$match`

Ici, c'est identique à celle du paramètre `query` des autres fonctions

- Idem en se restreignant à *Brooklyn*
  - Notez que nous obtenons uniquement 5 restaurants au final

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $sort: { name: 1 }},
    { $match: { borough: "Brooklyn" }}
]).pretty()
```

- Mêmes opérations, mais avec la restriction en amont de la limite
  - Nous avons ici les 10 premiers restaurants de *Brooklyn* donc

```js
db.restaurants.aggregate([
    { $match: { borough: "Brooklyn" }},
    { $limit: 10 },
    { $sort: { name: 1 }}
]).pretty()
```

### `$unwind`

Le but de cette opération est d'**exploser** un tableau dans un document.

> Un document avec un tableau à *n* éléments deviendra *n* documents avec chacun un des éléments du tableau en lieu et place de celui-ci.

Nous devons mettre le nom du tableau servant de base pour le découpage (précédé d'un `$`)

- Séparation des 10 premiers restaurants sur la base des évaluations (`grades`)
  - Chaque ligne correspond maintenant à une évaluation pour un restaurant

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $unwind: "$grades" }
]).pretty()
```

- Idem précédemment, en se restreignant à celle ayant eu *B*

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $unwind: "$grades" },
    { $match: { "grades.grade": "B" }}
]).pretty()
```

- Si on inverse les opérations `$unwind` et `$match`, le résultat est clairement différent

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $match: { "grades.grade": "B" }},
    { $unwind: "$grades" }
]).pretty()
```

### `$addFields` et  `$project`

On souhaite ici redéfinir les documents en ajoutant des éléments (`$addFields`) ou en se restreignant à certains éléments
(`$project`)

- `{ "champs" : 1 }` : conservation du champ (0 si suppression - idem que dans `find()`, pas de mélange sauf pour `_id`)
  - valable uniquement dans `$project`
- `{ "champs": { "$opérateur" : expression }}` : permet de définir un nouveau champ
- `{ "nouveau_champs": "$ancien_champs" }` : renommage d'un champ

Quelques opérateurs utiles pour la projection (plus d'info [ici](https://docs.mongodb.com/manual/reference/operator/aggregation/))

- `$arrayElemAt` : élément d'un tableau
- `$first` et `$last` : premier ou dernier élément du tableau
- `$size` : taille d'un tableau
- `$substr` : sous-chaîne de caractères
- `$cond` : permet de faire une condition (genre de *if then else*)
- ...
- On peut aussi vouloir ajouter un champ, comme ici le nombre d'évaluations

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $addFields: { nb_grades: { $size: "$grades" } } }
]).pretty()
```

- On souhaite ici ne garder que le nom et le quartier des 10 premiers restaurants
  - Notez l'ordre (alphabétique) des variables, et pas celui de la déclaration

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $project: { name: 1, borough: 1 } }
]).pretty()
```

- Ici, on supprime l'adresse et les évaluations

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $project: { address: 0, grades: 0 } }
]).pretty()
```

- En plus du nom et du quartier, on récupère l'adresse, mais dans un nouveau champ

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $project: { name: 1, borough: 1 , street: "$address.street"} }
]).pretty()
```

- On ajoute le nombre de visites pour chaque restaurant (donc la taille du tableau `grades`)

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $project: { name: 1, borough: 1, nb_grades: { $size: "$grades" } } }
]).pretty()
```

- On trie ce résultat par nombre de visites, et on affiche les 10 premiers
  - Notez qu'il y a des restaurants sans visite donc (pour lesquels `grades` est présent, mais égal à `NULL`)
  - Dans l'idéal, ces restaurants ne devraient pas avoir de champs `grades`

```js
db.restaurants.aggregate([
    { $project: { name: 1, borough: 1, nb_grades: { $size: "$grades" } } },
    { $sort: { nb_grades: 1 }},
    { $limit: 10 }
]).pretty()
```

- On ne garde maintenant que le premier élément du tableau `grades` (indicé 0)

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $project: { name: 1, borough: 1, grade: { $arrayElemAt: [ "$grades", 0 ]} } }
]).pretty()
```

- On peut aussi faire des opérations sur les chaînes, tel que la mise en majuscule du nom

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $project: { nom: { $toUpper: "$name" }, borough: 1 } }
]).pretty()
```

- On extrait ici les trois premières lettres du quartier

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $project: { 
        nom: { $toUpper: "$name" }, 
        quartier: { $substr: [ "$borough", 0, 3 ] } 
    } }
]).pretty()
```

- On fait de même, mais on met en majuscule et on note *BRX* pour le *Bronx*
  - on garde le quartier d'origine pour vérification ici

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $addFields: { quartier: { $toUpper: { $substr: [ "$borough", 0, 3 ] } } }},
    { $project: { 
        nom: { $toUpper: "$name" }, 
        quartier: { $cond: { if: { $eq: ["$borough", "Bronx"] }, then: "BRX", else: "$quartier" } },
        borough: 1
    } }
]).pretty()
```

### `$group`

Cet opérateur permet le calcul d'agrégats tel qu'on le connaît.

- `_id` : déclaration du critère de regroupement

  - chaîne de caractères : pas de regroupement (tous les documents)
  - `$champs` : regroupement selon ce champ
  - `{ a1: "$champs1", ... }` : regroupement multiple (avec modification des valeurs possible)
- Calculs d'agrégats à faire :

  - `$sum` : somme (soit de valeur fixe - 1 pour faire un décompte donc, soit d'un champ spécifique)
  - `$avg, $min, $max`
  - `$addToSet` : regroupement des valeurs distinctes d'un champ dans un tableau
  - `$push` : agrégation de champs dans un tableau
- On calcule ici le nombre total de restaurants

```js
db.restaurants.aggregate([
    { $group: { _id: "Total", NbRestos: { $sum: 1 }}}
])
```

- On fait de même, mais par quartier

```js
db.restaurants.aggregate([
    { $group: { _id: "$borough", NbRestos: { $sum: 1 }}}
])
```

- Pour faire le calcul des notes moyennes des restaurants du *Queens*, on exécute le code suivant

```js
db.restaurants.aggregate([
    { $match: { borough: "Queens" }},
    { $unwind: "$grades" },
    { $group: { _id: "null", score: { $avg: "$grades.score" }}}
])
```

- Il est bien évidemment possible de faire ce calcul par quartier et de les trier selon les notes obtenues (dans l'ordre décroissant).

```js
db.restaurants.aggregate([ 
    { $unwind: "$grades" },
    { $group: { _id: "$borough", score: { $avg: "$grades.score" }}},
    { $sort: { score: -1 }}
])
```

- On peut aussi faire un regroupement par quartier et par rue (en ne prenant que la première évaluation - qui est la dernière en date a priori), pour afficher les 10 rues où on mange le plus sainement.
  - Notez que le premier `$match` permet de supprimer les restaurants sans évaluations (ce qui engendrerait des moyennes = `NA`)

```js
db.restaurants.aggregate([
    { $project: { 
        borough: 1, street: "$address.street", 
        eval: { $arrayElemAt: [ "$grades", 0 ]} 
    } },
    { $match: { eval: { $exists: true } } },
    { $match: { "eval.score": { $gte: 0 } } },
    { $group: { 
        _id: { quartier: "$borough", rue: "$street" }, 
        score: { $avg: "$eval.score" }
    }},
    { $sort: { score: 1 }},
    { $limit: 10 }
])
```

- Pour comprendre la différence entre `$addToSet` et `$push`, on les applique sur les grades obtenus pour les 10 premiers restaurants
  - `$addToSet` : valeurs distinctes
  - `$push` : toutes les valeurs présentes

```js
db.restaurants.aggregate([
    { $limit: 10 },
    { $unwind: "$grades" },
    { $group: { 
        _id: "$name", 
        avec_addToSet: { $addToSet: "$grades.grade" },
        avec_push: { $push: "$grades.grade" }
    }}
])
```

### `$sortBycount`

Cet opérateur réalise un regroupement sur le champ spécifié (précédé d'un `$`), compte le nombre de documents pour chaque
modalité de ce champ, puis fait un tri décroissant sur le nombre calculé. Il est clairement fait pour réaliser des TOPs donc.

- Quartiers de New-York triés par nombre décroissant de restaurants

```js
db.restaurants.aggregate([
    { $sortByCount: "$borough" }
])
```

- C'est l'équivalent de la commande suivante

```js
db.restaurants.aggregate([
    { $group: { _id: "$borough", count: { $sum: 1 } } },
    { $sort: { count: -1 }}
])
```

## A faire

1. Quelles sont les 10 plus grandes chaines de restaurants (nom identique) ?
   - TOP 10 classique (2 façons de faire donc)
     ```python
     response = customers.aggregate(
         [
             {"$group": {"_id": "$name", "count": {"$sum": 1}}},
             {"$sort": {"count": -1}},
             {"$limit": 10},
             {"$project": {"_id": 0, "name": "$_id", "count": 1}},
         ]
     )
     ```
2. Donner le Top 5 et le Flop 5 des types de cuisine, en termes de nombre de restaurants
   - idem, avec le tri qui change entre les 2 demandes

     ```python

     response = customers.aggregate(
         [
             {"$group": {"_id": "$cuisine", "count": {"$sum": 1}}},
             {"$sort": {"count": -1}}, #-1 décroissant donc top , 1 FLOP
             {"$limit": 5},
             {"$project": {"_id": 0, "cuisine": "$_id", "count": 1}},
         ]
     )
     ```
3. Quelles sont les 10 rues avec le plus de restaurants ?
   - TOP 10 aussi

     ```python
     response = customers.aggregate(
         [
             {"$group": {"_id": "$address.street", "count": {"$sum": 1}}},
             {"$sort": {"count": -1}},
             {"$limit": 10},
             {"$project": {"_id": 0, "street": "$_id", "count": 1}},
         ]
     )
     ```
4. Quelles sont les rues situées sur strictement plus de 2 quartiers ?
   - Essayez d'ajouter le nom des quartiers de chaque rue (cf `addToSet`)

     ```python
     response = customers.aggregate(
         [
             {"$group": {"_id": "$address.street", "boroughs": {"$addToSet": "$borough"}}},
             {"$match": {"boroughs.2": {"$exists": True}}},
             {"$project": {"_id": 0, "street": "$_id", "boroughs": 1}},
         ]
     )
     ```
5. Lister par quartier le nombre de restaurants et le score moyen
   - Attention à bien découper le tableau `grades `
     ```python
     response = customers.aggregate(
         [
             {"$unwind": "$grades"},
             {
                 "$group": {
                     "_id": "$borough",
                     "nombre_restaurants": {"$sum": 1},
                     "score_moyen": {"$avg": "$grades.score"},
                 }
             },
             {
                 "$project": {
                     "_id": 0,
                     "borough": "$_id",
                     "nombre_restaurants": 1,
                     "score_moyen": {"$round": ["$score_moyen", 4]},
                 }
             },
             {"$sort": {"nombre_restaurants": -1}},
         ]
     )
     ```
6. Donner les dates de début et de fin des évaluations
   - min et max sont dans un bateau
     ```python
     response = customers.aggregate(
         [
             {"$unwind": "$grades"},
             {
                 "$group": {
                     "_id": "$name",
                     "date_debut": {"$min": "$grades.date"},
                     "date_fin": {"$max": "$grades.date"}
                 }
             },
             {
                 "$project": {
                     "_id": 0,
                     "name": "$_id",
                     "date_debut": 1,
                     "date_fin": 1
                 }
             }
         ]
     )
     ```
7. Quels sont les 10 restaurants (nom, quartier, addresse et score) avec le plus petit score moyen ?
   - découpage, regroupement par restaurant, tri et limite
     ```python
     response = customers.aggregate(
         [
             {"$unwind": "$grades"},
             {
                 "$match": {
                     "$and": [{"grades.score": {"$ne": None}}, {"grades.score": {"$ne": 0}}]
                 }
             },
             {
                 "$group": {
                     "_id": "$name",
                     "borough": {"$first": "$borough"},
                     "address": {"$first": "$address.street"},
                     "score_moyen": {"$avg": "$grades.score"},
                 }
             },
             {"$sort": {"score_moyen": 1}},
             {"$limit": 10},
             {
                 "$project": {
                     "_id": 0,
                     "name": "$_id",
                     "borough": 1,
                     "address": 1,
                     "score_moyen": 1,
                 }
             },
         ]
     )
     ```
8. Quels sont les restaurants (nom, quartier et addresse) avec uniquement des grades "A" ?
   - restriction à ceux qui ont A, découpage, suppression des autres grades que "A" et affichage des infos
   - on peut envisager d'autres choses (découpage, `addToSet`, et restriction à ceux pour lequel le tableau créé = ["A"] - par exemple)
     ```python
     response = customers.aggregate(
         [
             {"$unwind": "$grades"},
             {"$match": {"grades.grade": "A"}},
             {
                 "$group": {
                     "_id": "$name",
                     "borough": {"$first": "$borough"},
                     "address": {"$first": "$address.street"},
                     "grades_set": {"$addToSet": "$grades.grade"},
                 }
             },
             {"$match": {"grades_set": ["A"]}},
             {"$project": {"_id": 0, "name": "$_id", "borough": 1, "address": 1}},
         ]
     )
     ```
9. Compter le nombre d'évaluations par jour de la semaine
   - petite recherche sur l'extraction du jour de la semaine à partir d'une date à faire
     ```python
     response = customers.aggregate(
         [
             {"$unwind": "$grades"},
             {
                 "$group": {
                     "_id": {"$dayOfWeek": "$grades.date"},
                     "nombre_evaluations": {"$sum": 1},
                 }
             },
             {"$project": {"_id": 0, "jour_semaine": "$_id", "nombre_evaluations": 1}},
             {"$sort": {"jour_semaine": 1}},
         ]
     )
     ```
10. Donner les 3 types de cuisine les plus présents par quartier
    - simple à dire, compliqué à faire
    - une piste
      1. double regroupement à prévoir
      2. tri à prévoir
      3. regroupement avec `push`
      4. `slice` pour prendre une partie d'un tableau

         ```python
         response = customers.aggregate(
             [
                 {
                     "$group": {
                         "_id": {"borough": "$borough", "cuisine": "$cuisine"},
                         "count": {"$sum": 1},
                     }
                 },
                 {
                     "$group": {
                         "_id": "$_id.borough",
                         "cuisines": {"$push": {"cuisine": "$_id.cuisine", "count": "$count"}},
                     }
                 },
                 {
                     "$project": {
                         "cuisines": {
                             "$slice": [
                                 {"$sortArray": {"input": "$cuisines", "sortBy": {"count": -1}}},
                                 3,
                             ]
                         }
                     }
                 },
             ]
         )
         ```
