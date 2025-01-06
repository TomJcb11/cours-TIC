from models.binary_calculator import BinaryCalculator
from models.complex_calculator import ComplexCalculator


def main():
    print("Starting the calculator...")

    print("Welcome to the calculator! chose the model")
    print("1. Binary Calculator for binary operations")
    print("2. Complex Calculator for more complex expressions")
    input_ = input("Enter your choice: 1/2   ")
    match input_:
        case "1":
            number_a = float(input("Enter the first number: "))
            number_b = float(input("Enter the second number: "))
            method = input(
                "Enter the method: addition/soustraction/division/multiplication/puissance/racine \n"
            )
            binary_calculator = BinaryCalculator(
                number_a, number_b, method, "binary_calculator.log"
            )

            binary_calculator.calculate()
            binary_calculator.log()
        case "2":
            calculator = ComplexCalculator(log_file="complex_calculator.log")
            calculator.calculate()
            calculator.log()
        case _:
            print("Invalid choice, please try again.")


main()
