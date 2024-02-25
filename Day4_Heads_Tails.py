import random 
Heads_or_Tails = random.randint(0, 1)
if Heads_or_Tails == 0: 
   print("Tails")
elif Heads_or_Tails == 1: 
   print("Heads")

# truthy / trufy und falsy - geht auch so!! immer wenn das Ergebnis 0/undefiniert/leer ist immer False
Heads_or_Tails = random.randint(0, 1)
if Heads_or_Tails: 
   print("Heads")
else: 
   print("Tails")