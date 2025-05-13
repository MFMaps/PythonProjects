import functools
from operator import sub, truediv

class Calculator:
    def __init__(self):
        self.number = 0
        self.numbers = []
        self.result = 0
        self.operator = ""
        self.chosen = False
    
    def get_numbers(self):
        while self.number != 'quit':
            self.number = input("(Type 'quit' to quit the while loop)\nEnter in a number to add to the equation: ")
            if self.number.isnumeric():
                self.number = int(self.number)
                self.numbers.append(self.number)
                print("Number has been added to the list.")
            elif self.number == 'quit':
                pass
            else:
                print(f"{self.number} is not an integer.")
        print("Numbers have been officially set")
    
    def set_operator(self):
        while self.chosen != True:
            operator_values = ['+', '-', '*', '/']
            self.operator = input("(Operator choices: '+', '-', '*', '/')\nChoose the operator you'd like to use on this list of numbers: ")
            if self.operator in operator_values:
                print(f"{self.operator} has been chosen.")
                self.chosen = True
            else:
                print("Invalid option. Choose again.")
        return self.operator
    
    def add_values(self):
        if not self.numbers == []:
            if self.operator == "+":
                self.result = 0
                for item in self.numbers:
                    self.result += item
            return f"The sum of these values is {self.result}."
        else:
            return 0
    
    def subtract_values(self):
        if not self.numbers == []:
            if self.operator == "-":
                self.result = functools.reduce(sub, self.numbers)
            return f"The difference of these values is {self.result}."
        else:
            return 0
    
    def multiply_values(self):
        if not self.numbers == []:
            if self.operator == "*":
                self.result = 1
                for item in self.numbers:
                    self.result *= item
            return f"The product of these values is {self.result}."
        else:
            return 0
    
    def divide_values(self):
        if not self.numbers == []:
            if self.operator == "/":
                self.result = functools.reduce(truediv, self.numbers)
                if str(self.result)[-2:] == ".0":
                    self.result = str(self.result).replace(".0", "")
                    return f"The result of these values is {self.result}."
                else:
                    return f"The result of these values is {self.result:.2f}."
        else:
            return 0