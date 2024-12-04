from datetime import datetime


class Soigneur:
    def __init__(self, nom, date_naissance, experience, animal_list=[]):
        self._nom = nom
        self._date_naissance = date_naissance
        self._experience = experience
        self._animal_list = animal_list

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @property
    def experience(self):
        return self._experience

    @property
    def nombre_animaux_responsable(self):
        return len(self._animal_list)

    @property
    def age(self):
        today = datetime.today()
        birthdate = datetime.strptime(self._date_naissance, "%Y-%m-%d")
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        return age

    def find_animal_by_healer(self):
        animal_list_str = "\n".join([
            f"{i + 1}. {animal.name}" for i, animal in enumerate(self._animal_list)
        ])
        return animal_list_str

    def __str__(self):
        animal_list_str = self.find_animal_by_healer()
        return f"{self.nom} a pour caractéristiques : \n Age: {self.age} \n Années d'expérience: {self.experience} \n - Animaux sous sa garde: {self.nombre_animaux_responsable} \n - Liste des Animaux : \n{animal_list_str}"

    def nourrir(self, animal):
        if animal.en_vie and animal.manger(self.nom):
            print(f"{self.nom} nourrit {animal.nom} 🍽️")
        else:
            print(f"L'animal {animal.nom} est mort, il ne peut pas être nourri.")

    def entretenir(self, animal):
        if animal.en_vie:
            animal.bonheur = 100
            print(f"{self.nom} entretient {animal.nom} 💟")
        else:
            print(f"L'animal {animal.nom} est mort, il ne peut pas être entretenu....")
