class Gift:
    # region constructor
    def __init__(self, name, value, stock=1):
        self._name = name
        self._value = value
        self._stock = stock

    def __str__(self):
        return f"{self.name} pour({self.value} points de karma) - {self.stock} en stock"

    # endregion
    # region properties
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Le nom ne peut pas être vide")
        else:
            self._name = name

    @property
    def value(self):
        return self._name

    @value.setter
    def value(self, value):
        if value > 0 and value <= 10:
            self._value = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if stock < 0:
            raise ValueError("Le stock ne peut pas être négatif")
        else:
            self._stock = stock

    # endregion

    # region methods
    def remove_from_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Il n'y a pas assez de stock")
        else:
            self.stock -= quantity
