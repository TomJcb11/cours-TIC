class Animal:
    """# exo

    créer un petit programme de vetérinaire qui vous permet de gérer vos animaux

    - Vous pouvez entrer un nouvel animal (race, nom, age, couleur, .....)
    - Vous pouvez sortir un animal (seulement s'il est vacciné)
    - Vous pouvez vacciner un animal
    - Vous pouvez voir la liste des animaux (on doit savoir s'il est vacciné)

    """

    def __init__(
        self,
        name,
        species,
        birthdate,
        color,
        weight,
        vaccine=False,
    ):
        self.name = name
        self.species = species
        self.birthdate = birthdate
        self.color = color
        self.weight = weight
        self.vaccine

    def vaccine(self):
        self.vaccine = True
        print("Animal vaccinated")

    def return_animal(self):
        if self.vaccine:
            self.status = "out"
            print("Animal realeased")
        else:
            print("Animal not ready to be realeased")
