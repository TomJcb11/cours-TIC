# Centre d'examen d'une auto-école

Une auto-école souhaite construire une base de données pour gérer les examens théoriques du code de la route de ses élèves. Chaque élève est identifié par un numéro unique et est caractérisé par un nom, un prénom, une adresse et une date de naissance. Chaque élève assiste à plusieurs séances de cours sur le code de conduite (autant qu'il le souhaite). Chaque séance est caractérisée par une date et une heure. À chaque séance de cours, le directeur de l'auto-école choisit une série de questions sur un CD-ROM.

Chaque CD-ROM est identifié par un numéro et est caractérisé par un nom d'éditeur. Chaque CD-ROM est composé de 6 séries, numérotées de 1 à 6. Chaque série est composée de 40 questions. Chaque question est identifiée par un intitulé et est caractérisée par une réponse, un niveau de difficulté et un thème particulier. Une même question peut apparaître dans plusieurs séries avec un numéro d'ordre pour chaque série : par exemple, une même question peut apparaître comme question N°2 dans la série 5 du CD-ROM 15 et comme question N°12 dans la série 3 du CD-ROM 4. Une même série peut être projetée plusieurs fois à des séances différentes.

Lorsqu'un élève assiste à une séance, on retient le nombre de fautes qu'il a faites pour la série passée pendant la séance. Lorsqu'un élève a obtenu, au cours des quatre dernières séances auxquelles il a assisté, un nombre de fautes inférieur ou égal à 5, le directeur de l'auto-école l'autorise à passer l'examen théorique du code de la route à une date donnée (un seul examen pour une date donnée). L'auto-école ne peut présenter que 8 élèves maximum à chaque date d'examen. Les élèves ayant obtenu plus de 5 fautes à l'examen sont recalés et doivent assister de nouveau à des séances de code avant de pouvoir se représenter à l'examen.

La base de données doit permettre de répondre à des requêtes telles que :

- "Quel est le nombre moyen de fautes pour la série 5 du CD-ROM 14 ?"
- "Quels élèves peuvent se présenter au prochain examen du code de la route ?"
- "Quels élèves ont échoué au moins une fois à l'examen ?"
