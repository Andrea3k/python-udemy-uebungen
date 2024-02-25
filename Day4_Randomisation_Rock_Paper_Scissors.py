# Mersenne Twister --> 
# Pseudorandom 
# Module = Methode = Funktionen (mit Parametern als Input) - in diesem Fall ist "random" eine Funktion

import random
random_integer = random.randint(1,10)
print(random_integer)


# random() generiert eine Zufallszahl zwischen 0 und 1 (also 0.00000000... und 0.999999...)
random_float = random.random()
print(random_float)