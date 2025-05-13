from calculations import Calculator
from time import sleep

calc = Calculator()

if __name__ == "__main__":
    calc.get_numbers()
    calc.set_operator()
    sleep(1)
    print("Running...")
    sleep(5)
    if calc.operator == "+":
        print(calc.add_values())
    elif calc.operator == "-":
        print(calc.subtract_values())
    elif calc.operator == "*":
        print(calc.multiply_values())
    elif calc.operator == "/":
        print(calc.divide_values())
    else:
        print("Error")