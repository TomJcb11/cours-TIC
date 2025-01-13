# Correction aggregation

#### Exo 1
Quelles sont les 10 plus grandes chaines de restaurants (nom identique) ?
- TOP 10 classique (2 façons de faire donc)
````js
db.getCollection("restaurants").aggregate([
    {$group: {_id: "$name", nb: {$sum: 1}}},
    {$sort: {nb: -1}},
    {$limit: 10},
    {$project: {"_id": false, "nom": "$_id"}}
])
````
#### Exo 2
Donner le Top 5 et le Flop 5 des types de cuisine, en termes de nombre de restaurants
- idem, avec le tri qui change entre les 2 demandes
````js
db.getCollection("restaurants").aggregate([
    {$group: {_id: "$name", nb: {$sum: 1}}},
    {$sort: {nb: -1}},
    {$limit: 5},
    {$project: {"_id": false, "nom": "$_id"}}
])
db.getCollection("restaurants").aggregate([
    {$group: {_id: "$name", nb: {$sum: 1}}},
    {$sort: {nb: 1}},
    {$limit: 5},
    {$project: {"_id": false, "nom": "$_id"}}
])
````
### Exo 3
Quelles sont les 10 rues avec le plus de restaurants ?
- TOP 10 aussi
````js
db.getCollection("restaurants").aggregate([
  {$group: {_id: "$address.street", nb: {$sum: 1}}},
  {$sort: {nb: -1}},
  {$limit: 10},
  {$project: {_id: false, nom: '$_id'}}
])
````
### Exo 4
Quelles sont les rues situées sur strictement plus de 2 quartiers ?
- Essayez d'ajouter le nom des quartiers de chaque rue (cf `addToSet`)
````js
db.getCollection("restaurants").aggregate([
  {$group: {_id: "$address.street", nb: {$addToSet: "$borough"}}},
  {$project: {
      _id: false,
      nom: '$_id',
      nb: { $gt: [ { $size: "$nb" }, 2 ] } 
  }},
  {$match: {nb: true}},
  {$project: {street: "$nom"}}
])
````
#### Exo 5
Lister par quartier le nombre de restaurants et le score moyen
- Attention à bien découper le tableau `grades`
````js
db.getCollection("restaurants").aggregate([
  {$unwind: "$grades"},
  {$group: {_id: "$borough", score: {$avg: "$grades.score"}, count: {$sum: 1}}},
])
````
#### Exo 6
Donner les dates de début et de fin des évaluations
- min et max sont dans un bateau
````js
db.getCollection("restaurants").aggregate([
    {$addFields: {
        "min": {$min: "$grades.date"}, 
        "max": {$max: "$grades.date"}
    }},
    {$project: {_id: false, name: true, min: true, max: true}}
])
````
#### Exo 7
Quels sont les 10 restaurants (nom, quartier, addresse et score) avec le plus petit score moyen ?
- découpage, regroupement par restaurant, tri et limite
````js
db.getCollection("restaurants").aggregate([
    {$unwind: "$grades"},
    {$match: {grades: {$exists: true}, "grades.score": {$ne: null}}},
    {$group: {_id: {nom: "$name", quartier: "$borough", adresse: "$address"} , score: {$avg: "$grades.score"}}},
    {$sort: {score: 1}},
    {$limit: 10},
    {$project: {_id: false, "nom": "$_id.nom", "quartier": "$_id.quartier", "adresse": "$_id.adresse", score: true}}
])
````
#### Exo 8
Quels sont les restaurants (nom, quartier et addresse) avec uniquement des grades "A" ?
- restriction à ceux qui ont A, découpage, suppression des autres grades que "A" et affichage des infos
- on peut envisager d'autres choses (découpage, `addToSet`, et restriction à ceux pour lequel le tableau créé = ["A"] - par exemple)
````js
db.getCollection("restaurants").aggregate([
    {$unwind: "$grades"},
    {$group: {_id: {nom: "$name", quartier: "$borough", adresse: "$address"} , grades: {$addToSet: "$grades.grade"}}},
    {$match: {grades: {$in: ["A"], $size: 1}}},
    {$project: {_id: false, "nom": "$_id.nom", "quartier": "$_id.quartier", "adresse": "$_id.adresse"}}
])
````
#### Exo 9
Compter le nombre d'évaluations par jour de la semaine
- petite recherche sur l'extraction du jour de la semaine à partir d'une date à faire
````js
db.getCollection("restaurants").aggregate([
    {$unwind: "$grades"},
    {$group: {_id: {day: {$dayOfWeek: "$grades.date"}}, sum: {$sum: 1}}},
    {$project: {"day": "$_id.day", sum: true}}
])
````
#### Exo 10
Donner les 3 types de cuisine les plus présents par quartier
- simple à dire, compliqué à faire
- une piste
    1. double regroupement à prévoir
    2. tri à prévoir
    3. regroupement avec `push`
    4. `slice` pour prendre une partie d'un tableau
````js
// db.getCollection("restaurants").aggregate([
//   {$project: {_id: true, borough: true, cuisines: {$split: ["$cuisine", ","]}}},
//   {$unwind: "$cuisines"},
//   {$group: {_id: { cuisine: "$cuisines", borough: "$borough"}, count: {$sum: 1}}},
//   {$sort: {count: 1}}
// ])
````