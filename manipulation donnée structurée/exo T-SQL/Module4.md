# 4. Boucle et Curseurs

## 4.1 Est-il possible de sortir d’une boucle WHILE en T-SQL ? Si oui comment ?

Testez cette possibilité avec une boucle qui affiche le carré des nombres de 1 à 20 mais qui sort de la boucle si la valeur vaut 12.

```sql
DECLARE @i INT
SET @i = 1

WHILE (@i <= 20 )
	BEGIN
		IF ((@i = 12) BREAK
		PRINT (@i * @i)
		SET @i = @i + 1 
	END
```

## 4.2 Comment mettre fin à une boucle en T-SQL ?

Créez une boucle WHILE infinie.

* Cela fait-il planter SQLServer ? NON
* Quels sont les 2 choses les plus importantes ?
  * l'incrémentation
  * une condition de sortie

```sql
DECLARE @j INT = 2
WHILE @j > 0
	BEGIN
		print @j
		set @j = @j*@j
	END
```

## 4.3 Afficher le carré des nombres impairs allant de 1 à 50 sans prendre les nombres compris entre 20 et 30.

```sql
DECLARE @j INT = 1
WHILE @j <= 50
	BEGIN
	if (@j %2 = 1 AND @j NOT BETWEEN 20 AND 30)
		print POWER(@j,2)
		set @j = @j+1
	END
```

## 4.4 Écrire une boucle WHILE qui affiche la phrase « Ceci est un nombre divisible par 3 : [valeur_divisible_par_3] » pour tous les nombres divisibles par 3 entre 1 et 30.

```sql
DECLARE @j INT = 1
WHILE @j <= 30
	BEGIN
	if (@j %3 = 0)
		BEGIN
			print (CONVERT(VARCHAR,@j) + ' est un multiple de 3')
			set @j = @j+1
		END
	END
```

## 4.5 Écrire une boucle WHILE qui affiche le décompte des années depuis aujourd’hui jusqu’à 1983. Incrémenter également un compteur à afficher en fin de décompte dans la phrase « [compteur] années ont été décomptées depuis [annee_en_cours] ».

```sql
DECLARE  @annee INT, @counter INT
set @annee = YEAR(GETDATE())
set @counter = 0
WHILE @annee >= 1983
	BEGIN
		SET @annee = @annee - 1
		SET @counter = @counter + 1
	END
PRINT 'Entre 1983 et ' + CONVERT(VARCHAR,YEAR(GETDATE()))  +' ,'+
CONVERT(VARCHAR,@counter) + ' années se sont écoulées'
```

## 4.6 Écrire une boucle qui, pour chaque itération, enregistre la date sous 5 formats différents (vous avez le choix des formats) dans une variable de type TABLE. Afficher les données récoltées à l’écran.

Pensez ici aux formats de dates pour CONVERT ainsi qu’à la fonction RAND()…

```sql
DECLARE @formats TABLE(date VARCHAR(50))
DECLARE @counter INT = 0


WHILE @counter <=5
	BEGIN
		INSERT INTO @formats VALUES (CONVERT(
										VARCHAR,
										GETDATE(),
										CONVERT(INT,100+(RAND()*14))
											)
									)
		SET @counter +=1
	END
SELECT * from @formats
```

## 4.7 Écrire une boucle simple qui permette d’afficher la phrase « [LAST_NAME de l’employé] est l’employé dont l’id est [ID de l’employé] » pour les 100 premiers employés de la table « Person.Person ».

Faites l’exercice en déclarant d’abord 2 variables distinctes de type table "tab_nom" qui contiendront les valeurs pour LastName et BusinessEntityId (sans utiliser de curseur) et l'autre "tab_id" qui contiendra le BusinessEntityId (Utiliser une jointure pour afficher les résultats). Refaire ensuite l’exercice en stockant d’abord les valeurs récupérées dans un curseur.

### Version sans cursor

```sql
DECLARE @tab_nom table (BusinessEntityID INT,LastName VARCHAR(50))
DECLARE @tab_id table (BusinessEntityID INT)

insert into @tab_nom select BusinessEntityID, LastName
from person.Person

insert into @tab_id select BusinessEntityID
from person.Person

--SELECT top 100 * from @tab_nom order by BusinessEntityID
--SELECT top 100 * from @tab_id order by BusinessEntityID
 SELECT TOP 100
	nom.LastName + ' est l''employé dont l''id est '+ CONVERT(VARCHAR,id.BusinessEntityID)
 from @tab_nom as nom join @tab_id as id on nom.BusinessEntityID = id.BusinessEntityID



```

### Version avec un cursor

```sql
DECLARE @id INT, @nom VARCHAR(50)
DECLARE CR_employees CURSOR 
	for SELECT TOP 100 BusinessEntityID,LastName from Person.Person
OPEN CR_employees
FETCH CR_employees into @id,@nom
while @@FETCH_STATUS = 0
	BEGIN
		PRINT @nom +' est l''employé dont l''id est '+ CONVERT(VARCHAR,@id)
		FETCH CR_employees into @id,@nom
	END

CLOSE CR_employees
DEAlLOCATE CR_employees
```

## 4.8 Récupérer les 200 premiers noms, prénoms et ID d’employés de la table Person.Person ainsi que leur Job à partir de la table HumanResources.Employees. Stocker ces valeurs dans un curseur. Afficher les données du curseur dans une table temporaire, mais uniquement si ces valeurs correspondent aux employés techniciens de productions WC60. Le tri se fera après récupération de l’ensemble des données dans le curseur.


## 4.9 Afficher les données des employés (Nom, Prénom, Date de naissance) rattachés à l’un des Jobs (Janitor). Assurez-vous qu’il ne faille changer les données que d’une seule variable afin d’afficher les données des employés rattachés à un autre Job.

## 4.10 Récupérer la liste des Id d'employés dans un curseur.

Récupérer la liste des ventes de la table Sales.SalesPerson dans un autre curseur. Pour chaque employé, si son id (BusinessEntityId) est reprise dans le second curseur, afficher le montant de la dernière commission qui le concerne et la date à laquelle elle a été modifiée. Attention, tout se passe avec les curseurs et les boucles, pas question de faire de jointure dans ce cas !

## 4.11 Récupérer les produits et leurs noms dans la table Production.Product dans un premier curseur.

Récupérer la quantité commandée des produits dans la table Production.Workorder dans un second curseur. Pour chaque produit existant, afficher la quantité commandée. Attention, pas de COUNT via un SELECT dans ce cas ! De nouveau, tout se passe dans les curseurs et les boucles ! Ne tester la requête que pour les 2000 premières entrées de la table Production.Workorder.

## 4.12 Récupérer le prix le plus récent (pas de date de fin EndDate) de chacun des produits dans la table Production.productCostHistory.

Récupérer dans un autre curseur les données concernant chaque produit. Pour chaque produit, insérer dans une table temporaire son nom, son prix et la date de sa dernière mise à jour.
