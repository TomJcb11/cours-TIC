import math

from models.super_calculator import SuperCalculator


class BinaryCalculator(SuperCalculator):
    """A calculator for binary operations.""
    Only supports addition, soustraction, multiplication, division, power and root.
    Args:
        SuperCalculator (_type_): _description_
    """

    instance_counter = 0

    def __init__(self, number_a, number_b, method, log_file):
        super().__init__(log_file)
        self.number_a = number_a
        self.number_b = number_b
        self.method = method
        BinaryCalculator.instance_counter += 1
        self.instance_number = BinaryCalculator.instance_counter
        self.log_file = log_file

    def calculate(self):
        try:
            result = {
                "addition": self.number_a + self.number_b,
                "soustraction": self.number_a - self.number_b,
                "multiplication": self.number_a * self.number_b,
                "division": self.number_a / self.number_b
                if self.number_b != 0
                else "Erreur: Division par zéro",
                "puissance": self.number_a**self.number_b,
                "racine": math.sqrt(self.number_a),
            }.get(self.method, "Erreur: Méthode inconnue")
            return result
        except Exception as e:
            return f"Erreur: {str(e)}"

    def log(self):
        with open(self.log_file, "a") as file:
            self.count_lines_in_file()  # check the file len
            print("adding entry to log file...")
            file.write(
                f"{self.number_a} {self.method} {self.number_b} = {self.calculate()}\n"
            )
