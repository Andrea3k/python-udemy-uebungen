# building a calculator
# "return" ist das Ende der Funktion, alles danach wird nich mehr ausgeführt
# mit return kann man auch die function frühzeitig beenden/escapen

first_name = input("What is your first name?")
last_name = input("What is you last name?")

def format_name(first_name, last_name):
    first_name = first_name.title()
    last_name = last_name.title()
    name = first_name + " " + last_name
    return name

name_title = format_name(first_name, last_name)
print(name_title)

