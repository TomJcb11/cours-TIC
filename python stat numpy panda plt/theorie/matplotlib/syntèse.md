# Chapitre 1 : Définitions des Variables Qualitatives et Quantitatives

## Variables Qualitatives

Les variables qualitatives, également appelées variables catégorielles, sont des variables qui décrivent une qualité ou une caractéristique. Elles ne sont pas numériques et ne peuvent pas être mesurées. Elles se divisent en deux sous-catégories :

### Variables Nominales

* **Définition** : Variables catégorielles sans ordre intrinsèque.
* **Exemples** : Couleur des yeux (bleu, vert, marron), type de voiture (SUV, berline, coupé).
* **Visualisation** : Diagramme circulaire (pie chart), diagramme en barres (bar chart).

### Variables Ordinales

* **Définition** : Variables catégorielles avec un ordre intrinsèque.
* **Exemples** : Niveau d'éducation (primaire, secondaire, universitaire), classement dans une compétition (premier, deuxième, troisième).
* **Visualisation** : Diagramme en barres (bar chart), boxplot.

## Variables Quantitatives

Les variables quantitatives sont des variables qui peuvent être mesurées et exprimées numériquement. Elles se divisent en deux sous-catégories :

### Variables Discrètes

* **Définition** : Variables numériques qui prennent des valeurs distinctes et séparées.
* **Exemples** : Nombre d'enfants dans une famille, nombre de voitures possédées.
* **Visualisation** : Histogramme, diagramme en barres (bar chart), ECDF (Empirical Cumulative Distribution Function).

### Variables Continues

* **Définition** : Variables numériques qui peuvent prendre une infinité de valeurs dans un intervalle donné.
* **Exemples** : Taille, poids, température.
* **Visualisation** : Histogramme, boxplot, ECDF.

## Implémentation en Python

Voici comment vous pouvez manipuler et visualiser ces types de variables en Python en utilisant des bibliothèques comme `pandas`, `matplotlib` et `seaborn`.

### Exemple de Code

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Création d'un DataFrame exemple
data = {
    'Couleur des yeux': ['bleu', 'vert', 'marron', 'bleu', 'marron'],
    'Niveau d\'éducation': ['primaire', 'secondaire', 'universitaire', 'secondaire', 'primaire'],
    'Nombre d\'enfants': [2, 3, 1, 4, 2],
    'Taille': [1.75, 1.80, 1.65, 1.70, 1.68]
}
df = pd.DataFrame(data)

# Visualisation des variables qualitatives
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.countplot(x='Couleur des yeux', data=df)
plt.title('Couleur des yeux')

plt.subplot(1, 2, 2)
sns.countplot(x='Niveau d\'éducation', data=df)
plt.title('Niveau d\'éducation')
plt.show()

# Visualisation des variables quantitatives
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['Nombre d\'enfants'], bins=5, kde=False)
plt.title('Nombre d\'enfants')

plt.subplot(1, 2, 2)
sns.histplot(df['Taille'], bins=5, kde=True)
plt.title('Taille')
plt.show()
```


# Chapitre 2 : Concepts des Statistiques Descriptives

## Introduction

Les statistiques descriptives sont des outils utilisés pour résumer et décrire les caractéristiques principales d'un ensemble de données. Elles permettent de comprendre la distribution, la tendance centrale et la dispersion des données.

## Mesures de Tendance Centrale

Les mesures de tendance centrale indiquent où se situe le centre des données.

### Moyenne (arithmétique)

* **Définition** : La somme des valeurs divisée par le nombre de valeurs.
* **Formule** : [ \text{mean}(X) = \bar{x} = \frac{\sum_{i=1}^{N} x_i}{N} ]
* **Propriétés** : Sensible aux valeurs extrêmes.
* **Implémentation en Python** :

  ```python
  import numpy as np
  data = [0, 1, 1, 2, 3, 5, 8]
  mean_value = np.mean(data)
  print("Moyenne:", mean_value)

  ```

### Médiane

* **Définition** : La valeur centrale d'un ensemble de données triées.
* **Propriétés** : Robuste aux valeurs extrêmes.
* **Implémentation en Python** :

  ```python
  median_value = np.median(data)
  print("Médiane:", median_value)
  ```

### Mode

* **Définition** : La valeur la plus fréquente dans un ensemble de données.
* **Implémentation en Python**

  ```python
  from scipy import stats
  mode_value = stats.mode(data)
  print("Mode:", mode_value)
  ```


## Mesures de Dispersion

Les mesures de dispersion indiquent la variabilité ou la dispersion des données.

### Amplitude

* **Définition** : La différence entre la valeur maximale et minimale.
* **Formule** : [ \text{range}(X) = \max(X) - \min(X) ]
* **Implémentation en Python** :

  ```python
  range_value = np.max(data) - np.min(data)
  print("Amplitude:", range_value)
  ```

### Déviation Absolue Moyenne

* **Définition** : La moyenne des écarts absolus par rapport à la moyenne.
* **Formule** : [ \text{mad}(X) = \frac{\sum_{i=1}^{N} |x_i - \bar{x}|}{N} ]
* **Implémentation en Python** :

  ```python
  mad_value = np.mean([np.abs(x - np.mean(data)) for x in data])
  print("Déviation Absolue Moyenne:", mad_value)
  ```

### Variance et Écart-Type

* **Définition** : La variance est la moyenne des carrés des écarts par rapport à la moyenne, et l'écart-type est la racine carrée de la variance.
* **Formules** : [ \text{var}(X) = \frac{\sum_{i=1}^{N} (x_i - \bar{x})^2}{N} ] [ \text{std}(X) = \sqrt{\text{var}(X)} ]
* **Implémentation en Python** :

  ```python
  variance_value = np.var(data)
  std_dev_value = np.std(data)
  print("Variance:", variance_value)
  print("Écart-Type:", std_dev_value)
  ```

### Quartiles et Écart Interquartile (IQR)

* **Définition** : Les quartiles divisent les données en quatre parties égales, et l'IQR est la différence entre le troisième et le premier quartile.
* **Formules** : [ Q1 = \text{25ème percentile}, \quad Q3 = \text{75ème percentile} ] [ \text{IQR} = Q3 - Q1 ]
* **Implémentation en Python** :

  ```python
  Q1 = np.percentile(data, 25)
  Q3 = np.percentile(data, 75)
  IQR = Q3 - Q1
  print("IQR:", IQR)
  ```

## Visualisation des Données

Les graphiques sont des outils essentiels pour visualiser les statistiques descriptives.

### Histogramme

* **Utilisation** : Visualiser la distribution des données quantitatives.
* **Implémentation en Python** :

  ```python
  import matplotlib.pyplot as plt
  plt.hist(data, bins=5)
  plt.title("Histogramme")
  plt.show()
  ```

### Boxplot

* **Utilisation** : Visualiser la distribution des données et identifier les valeurs aberrantes.
* **Implémentation en Python** :

  ```python
  sns.boxplot(data)
  plt.title("Boxplot")
  plt.show()
  ```

### Diagramme en Barres

* **Utilisation** : Visualiser la distribution des données qualitatives.
* **Implémentation en Python** :

  ```python
  sns.countplot(x='Couleur des yeux', data=df)
  plt.title('Couleur des yeux')
  plt.show()
  ```
