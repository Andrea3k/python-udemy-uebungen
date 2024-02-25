input = "Angela, Ben, Jenny, Michael, Cloe"
# Delimiter --> text bzw. sting aufteilen über split
names = input.split(", ")
amount_of_bankers = len(names)
import random 
random_banker = random.randint(0, amount_of_bankers-1)
paying_banker = names[random_banker]
print(paying_banker)