# arguments --> das was in den klammern steht
# statements --> das was in der Funktion steht, also die Schritte, die in der Funktion ausgeführt werden

# Parameter = "name"
# Argument = "Angela"


def greet(): 
    print("Hello")
    print("How do you do?")
    print("Isn't the wather nice today")

greet()


def greet_with_name(name): 
    print(f"Hello {name}")
    print(f"How do you do? {name}?")

greet_with_name("Angela")


# Standardwert hinterlegen:

def greet_with_name(name = "Angela"): 
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Billy")

# functions with more than 1 input 
# positional arguments (die Reihenfolge der Parameter in der Funktion müssen beim Aufrufen der Funktion auch in der Reihenfolge mit Argumenten befüllt werden)

def greet_with(name, location): 
    print(f"Hi {name}, are you at {location}")

greet_with("Angela", "home")

# keyword arguments --> mit "=" kann man in der Funktion den Parametern default Werte einsetzen

def greet_with(name = "homie", location = "home"): 
    print(f"Hi {name}, are you in {location}")

greet_with(location = "New York")

# man kann beim Aufrufen der Funktion, die Parameter NUR weglassen bzw. keinen Wert zuweisen, wenn ein Default Wert gesetzt ist. 
