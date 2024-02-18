print("Welcome to treasure island!\nYour mission is to find the treasure.")
input_1 = input("Do you wanna go left or right?\n").lower()
if input_1 == "right": 
    print("GAME OVER")
elif input_1 == "left":
    input_2 = input("Do you wanna swim or wait?\n").lower()
    if input_2 == "swim":
        print("GAME OVER")
    elif input_2 == "wait": 
        input_3 = input("Which door do you choose? blue, yellow or red?\n").lower()
        if input_3 == "yellow": 
            print("YOU WIN!")
        elif input_3 == "red" or input_3 == "blue": 
            print("GAME OVER")