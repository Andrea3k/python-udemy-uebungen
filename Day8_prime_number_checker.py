def prime_checker(number):
    if number == 0: 
        print(f"{number} is not defined!")
        return False
    elif number == 1:
        print(f"{number} is not a prime number!")
        return False 
    else:
        for i in range(2, number//2 + 1):
            if number%i == 0: 
                print(f"Die Zahl {number} ist keine Primzahl!")
                return False
        print(f"{number} ist eine Primzahl!")
        return True 

n = int(input()) # Check this number
prime_checker(number = n) 

# nur durch primzahlen teilen wäre schöner 2, 3 ,5, 7, 11
# continue 