from abc import ABC, abstractmethod


class SuperCalculator(ABC):
    """An abstract base class for calculator.

    Args:
        - ABC (_type_): import of the abstract base class module

    Methods:
        - calculate(self): abstract method to calculate the result of the operation
        - log(self): abstract method to log the operation in a file
        - count_lines_in_file(self): method to check the number of lines in the log file
    """

    def __init__(self, log_file):
        self.log_file = log_file

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def log(self):
        pass

    def count_lines_in_file(self):
        with open(self.log_file, "r") as file:
            lines = file.readlines()
            if len(lines) >= 10:
                print("File contains more than 10 lines, erasing oldest entries")
                lines = lines[1:]
