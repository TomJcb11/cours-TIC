# Récapitulatif

## Données

Nous allons utiliser les données [world.json](../datasets/world.json), recensant les pays du monde (en l'état à la fin du siècle dernier). Pour pouvoir les utiliser, vous devez réaliser les étapes suivantes :

1. Télécharger le fichier <world.json>
2. Dans *Compass*, créer une base de données `test` et une collection `world`
3. Importer les données dans cette collection
4. Vérifier que tout est ok en lancant le shell
    - vous devriez avoir 239 documents

Voici une description des informations contenues dans les documents. **Tous les pays n'ont pas forcément tous les champs renseignés**.

- `Code`: code du pays en 3 lettres,
- `Name`: nom du pays,
- `Continent`: continent,
- `Region`: région (au sens partie d'un continent),
- `SurfaceArea`: superficie,
- `IndepYear`: année d'indépendance (si absent : pays dépendant d'un autre),
- `Population`: population totale,
- `LifeExpectancy`: espérance de vie,
- `GNP`: PIB,
- `GNPOld`: PIB ancien,
- `LocalName`: nom dans la langue du pays,
- `GovernmentForm`: type de gouvernement,
- `HeadOfState`: personnage à la tête de l'état,
- `Code2`: code du pays en 2 lettres,
- `Cities`: tableau décrivant les villes du pays connues dans la base
    - `Name`: nom de la capitale,
    - `District`: province/région,
    - `Population`: population de la ville,
    - `Capital` : `true` si c'est la capitale
- `Languages`: tableaux de langues dans le pays
    - `Language`: nom de la langue, 
    - `IsOfficial`: `true` si c'est une langue officielle (il peut y en avoir plusieurs)
    - `Percentage`: taux d'habitants du pays parlant cette langue,

## Demandes

1. Déterminer le nombre exact de pays
2. Lister les différents continents 
3. Lister les informations de la France
4. Lister les pays du continent européen, ayant une population inférieure à 100000 habitants 
5. Lister les pays indépendants du continent océanique
6. Quel est le plus gros continent en termes de surface ? (un seul continent affiché à la fin)
7. Donner par continents le nombre de pays, la population totale et en *bonus* le nombre de pays indépendant
8. Donner la population totale des villes de France 
9. Donner la capitale (uniquement nom de la ville et population) de France
10. Quelles sont les langues parlées dans plus de 15 pays ?
11. Calculer pour chaque pays le nombre de villes (pour les pays ayant au moins 100 villes), en les triant par ordre décroissant du nombre de villes
12. Lister les 10 villes les plus habitées, ainsi que leur pays, dans l'ordre décroissant de la population
13. Lister les pays pour lesquels le français est une langue officielle 
14. Lister les 5 pays avec le plus de langues parlées
15. Lister les pays pour lesquels la somme des populations des villes est supérieure à la population du pays 
     - ceci est probablement du à une erreur dans la base
    