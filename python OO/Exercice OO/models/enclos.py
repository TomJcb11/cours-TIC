class Pen:
    def __init__(self, name, capacity, size):
        self.name = name
        self.capacity = capacity
        self.animals = []
        self.size = size

    def add_animal(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            return True
        else:
            return False

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f"{self.name} : {len(self.animals)}"

    def __repr__(self):
        return f"{self.name} : {len(self.animals)}"

    def __len__(self):
        return len(self.animals)
