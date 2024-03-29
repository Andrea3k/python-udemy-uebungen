# docstrings = documentation for the function (erscheint in der box, die erscheint, wenn man über sich mit dem cursor in der Klammer der function befindet)
# can be created for functions as well 
# müssen in der ersten Zeile nach der "def" function sein und muss mit """ beginnen und enden (hier darf über mehrere Zeilen geschrieben werden)

# calculator 

import os 

# Add
def add(summand1, summand2):
    return summand1 + summand2 

# subtract
def subtract(minuend, subtrahend):
    return minuend - subtrahend

# multiply
def multiply(factor1, factor2): 
    return factor1 * factor2

# divide
def divide(dividend, divisor):
    return dividend / divisor 


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number? \n"))
    again = "y"
    while again == "y": 
        print(f"Your first number is: {num1}")
        for operator in operations: 
                print(operator)
        operation_symbol = input("Pick an operator from above: ")
        num2 = float(input("What is the second number? \n"))
        for operator in operations: 
            if operation_symbol == operator: 
                answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        again = input(f"Type 'y' to continue calculating with {num1}, of type 'n' to exit: \n")
        if again == "y": 
            num1 = answer
        else: 
            os.system('cls')
            calculator()
            #man kann innerhalb einer Funktion die Funktion selbst wieder aufrufen (rekursive) ! hiermit produziert man einen endlos schleife = CRINGE

calculator()
