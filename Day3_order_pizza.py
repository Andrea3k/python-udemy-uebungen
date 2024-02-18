pizza_size = input("What size pizza do you want? S, M or L?\n")
add_peperoni = input("Do you want peperoni? Y or N\n") 
extra_cheese = input ("Do you want extra cheese? Y or N\n") 
pizza_S = 15
pizza_M = 20
pizza_L = 25
peperoni_S = 2
peperoni_ML = 3
cheese = 1
if pizza_size == "S": 
    bill = pizza_S
    if add_peperoni == "Y":
        bill = bill + peperoni_S
        if extra_cheese == "Y":
            bill = bill + cheese
elif pizza_size == "M": 
    bill = pizza_M 
    if add_peperoni == "Y":
        bill = bill + peperoni_ML
        if extra_cheese == "Y":
            bill = bill + cheese
elif pizza_size == "L": 
    bill = pizza_L
    if add_peperoni == "Y":
        bill = bill + peperoni_ML
        if extra_cheese == "Y":
            bill = bill + cheese
print(f"Thank you for choosing Python Pizza Deliveries!\n Your final bill is: ${bill}")

# mit .upper() wird der input immer in Großbuchstaben umewandelt
# pizza_size = input("What size pizza do you want? S, M or L?\n").upper() 
# bei else darf keine Bedingung stehen
# man braucht nicht zwingend ein else, um die das if statement zu beenden
# man kann so viele elif statements machen wie man will 
