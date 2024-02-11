print("Welcome guys!")
cityOfBirth = input("What is the city you were born?\n")
nameOfPet = input("What is your pets name?\n")
Combination = str(cityOfBirth) + " " + str(nameOfPet)
print("This is your band name: " + Combination)


# hier eine weitere methode - mit f beginnend nach print 
print(f"To honour your birthplace of {city} and your first pet being named {pet}, your ban name could be :\n {bandname}")

#noch eine mega Möglichkeit: 
print ("so your pets name was {} and you grew up in {}".format(pet, city))

# mit den Zahlen in den Klammern wird die Reihenfolge festgelegt, in der die Klammern eingefüllt werden 
print ("so your pets name was {1} and you grew up in {0}".format(pet, city))