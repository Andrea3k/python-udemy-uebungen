# loops
# For Loop - for x in y: 
# immmer mit Doppelpunkt beenden 
# x ist in diesem Fall ein einzelnes Element und y ist der Container 
# iterable objects sind list and dictionary 
# die Variable fruit wird nur in der For Schleife erkannt, ist nur hier definiert, außerhalb der Schleife wird fruit nicht gefunden

# fruits =["Apple", "Peach", "Pear"]
# for fruit in fruits: 
#     print(fruit)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


password = ""
for l in range(0, nr_letters): 
    letter = random.choice(letters)
    password += letter

for n in range(0, nr_numbers): 
    number = random.choice(numbers)
    password += number

for s in range(0, nr_symbols): 
    symbol = random.choice(symbols)
    password += symbol

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
for l in range(0, nr_letters): 
    letter = random.choice(letters)
    password += letter

for n in range(0, nr_numbers): 
    number = random.choice(numbers)
    password += number

for s in range(0, nr_symbols): 
    symbol = random.choice(symbols)
    password += symbol

password_list = list(password)
random.shuffle(password_list)

password_shuffle = ""
for x in password_list: 
    password_shuffle += x 

print(password_shuffle)