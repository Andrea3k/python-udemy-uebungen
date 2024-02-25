# rock paper scissors
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
your_choice = int(input())
import random
computers_choice = random.randint(0,2)
print("Your choice: ", your_choice)
print("Computers Choice: ", computers_choice)
if your_choice == computers_choice: 
    print("TRY AGAIN!")
elif your_choice + 1 == computers_choice: 
    print("YOU LOST!")
elif your_choice -2 == computers_choice: 
    print("YOU LOST")
else: 
    print("YOU WON!")


