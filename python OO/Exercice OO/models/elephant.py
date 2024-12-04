class Elephant:
    def __init__(
        self,
        healer_list=[],
        name="Dumbo",
        appetite=50,
        hapiness=50,
        alive: bool = True,
        pen=None,
    ):
        self.name = name
        self.healer_list = healer_list
        self.appetite = appetite
        self.hapiness = hapiness
        self.alive = alive
        self.pen = pen

    def feed(self):
        if self.appetite >= 100 and self.hapiness >= 100:
            self.appetite = 100
            print(f"{self.name} is already full")
        else:
            print(f"{self.name} is eating")
            self.hapiness += 10
            self.appetite += 10

    def add_healer(self, healer):
        if healer not in self.healer_list:
            self.healer_list.append(healer)

    def find_healer_by_animal(self):
        healer_list_str = "\n".join([
            f"{i + 1}. {healer.name}" for i, healer in enumerate(self.healer_list)
        ])
        return healer_list_str

    def __str__(self):
        healer_list_str = "\n".join([
            f"{i + 1}. {healer.name}" for i, healer in enumerate(self.healer_list)
        ])
        return f" L'éléphant {self.name} voici ses statistiques : \n - statut: {'vivant' if self.alive else 'mort'} \n - joie: {self.hapiness}% \n - faim: {self.appetite}% \n - enclos: {self.pen}\n - soigneurs : \n{healer_list_str}  "


if __name__ == "__main__":
    elephant1 = Elephant(
        name="Dumbo", healer_list=["Thomas", "Tom"], hapiness=50, appetite=50
    )
    print(elephant1)
    elephant1.feed()
