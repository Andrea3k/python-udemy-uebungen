# Rollercoaster height check
# <= oder >= higher/lower or equal to 
# != not equal to
# == equal to --> Vergleicht den Wert und speichtert nicht in den Wert die Variable
height = int(input("What is your hight in cm?\n"))
age = int(input("What is your age?\n"))
if height >= 120: 
    print("You can ride the rollercoaster!")
    if age < 12: 
        print("You have to pay 5€")
    elif age <= 18: 
        print("You have to pay 7€")
    elif age >=45 and age <=55: 
        print("You don't have to pay anything!")
    else:
        print("You have to pay 12€")
else: 
    print("Sorry, you are out!")