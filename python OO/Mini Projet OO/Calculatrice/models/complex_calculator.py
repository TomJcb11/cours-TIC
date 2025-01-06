import re

from models.super_calculator import SuperCalculator


class ComplexCalculator(SuperCalculator):
    """A calculator for complex operations.
    Uses the keyboard library to capture keyboard events.
    Only supports addition, soustraction, multiplication, division, power and root.

    Args:
        SuperCalculator (_type_): _description_
    """

    def __init__(self, log_file):
        super().__init__(log_file)
        self._expression = "-1"
        self._result = -1
        # TODO: default value for result

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, value):
        # Définir une expression régulière pour valider l'expression
        pattern = re.compile(r"^[0-9+\-*/^V().\s]+$")
        if pattern.fullmatch(value):
            self._expression = value
        else:
            raise ValueError("Invalid expression")

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        pattern = re.compile(r"^[-+]?[0-9]*\.?[0-9]+$")
        if pattern.fullmatch(str(value)):
            self._result = value
        else:
            raise ValueError("Invalid result")

    def retrieve_expression(self):
        self.expression = input("""Enter the expression in the following format: 
                           + for addition
                           - for soustraction
                           * for multiplication
                           / for division
                           ** for power
                           ( for opening parenthesis
                           ) for closing parenthesis
                           """)
        print(f"Expression: {self.expression}")

    def log(self):
        with open(self.log_file, "a") as file:
            file.write(f"{self.expression} = {self.result}\n")
            print(f"{self.expression} = {self.result}")

    def calculate(self):
        try:
            self.expression = self.retrieve_expression()
            self.result = eval(self.expression)
            self.log()

        except Exception as e:
            print("c'est la merde")
            print(f"Error: {str(e)}")
