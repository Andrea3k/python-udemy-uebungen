# Test, ob die eingegebene Nummer gerade oder ungerade ist
number = int(input("What number do you want to check?\n"))
modulo = number % 2
if modulo == 0:
    print("Your number is even!")
else: 
    print("Your number is odd!")