# prüfen, ob ein Jahr ein Schaltjahr ist
year = int(input("What year do you want to test?\n"))
if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is a leap year!")
        else: 
            print("This year is NOT a leap year!")
    else: 
        print("This year is a leap year!")
else: 
    print("This year is NOT a leap year!")