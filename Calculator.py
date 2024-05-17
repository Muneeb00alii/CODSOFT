import os

class Calculator:
    def add(self, a, b):
        result = a + b
        return result

    def subtract(self, a, b):
        result = a - b
        return result

    def multiply(self, a, b):
        result = a * b
        return result

    def divide(self, a, b):
        result = a / b
        return result

    def square(self, a):
        result = a ** 2
        return result

    def cube(self, a):
        result = a ** 3
        return result

    def power(self, a, b):
        result = a ** b
        return result

    def square_root(self, a):
        result = a ** 0.5
        return result

    def cube_root(self, a):
        result = a ** (1/3)
        return result

    def n_root(self, a, b):
        result = a ** (1/b)
        return result


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("*"*25)
    print("Calculator\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Any Power")
    print("8. Square Root")
    print("9. Cube Root")
    print("10. Nth Root")
    print("11. Exit")
    print("*"*25)


def main():
    cal = Calculator()
    clear()
    while True:
        choice = input("Choose Any Function: ")

        if choice.lower() == "add" or choice == "1":
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result: ", cal.add(a, b))
        
        if choice.lower() == "subtract" or choice == "2":
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result: ", cal.subtract(a, b))
        
        if choice.lower() == "multiply" or choice == "3":
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result: ", cal.multiply(a, b))
        
        if choice.lower() == "divide" or choice == "4":
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
            print("Result: ", cal.divide(a, b))

        if choice.lower() == "square" or choice == "5":
            a = float(input("Enter the Number: "))
            print("Result: ", cal.square(a))

        if choice.lower() == "cube" or choice == "6":
            a = float(input("Enter the Number: "))
            print("Result: ", cal.cube(a))

        if choice.lower() == "any power" or choice == "7":
            a = float(input("Enter the Number: "))
            b = float(input("Enter the power: "))
            print("Result: ", cal.power(a, b))

        if choice.lower() == "square root" or choice == "8":
            a = float(input("Enter the Number: "))
            print("Result: ", cal.square_root(a))

        if choice.lower() == "cube root" or choice == "9":
            a = float(input("Enter the Number: "))
            print("Result: ", cal.cube_root(a))

        if choice.lower() == "nth root" or choice == "10":
            a = float(input("Enter the Number: "))
            b = float(input("Enter the power: "))
            print("Result: ", cal.n_root(a, b))

        if choice.lower() == "exit" or choice == "11":
            input("Press Enter to Exit")
            break

        else:
            print("Invalid Choice")
            continue

main()