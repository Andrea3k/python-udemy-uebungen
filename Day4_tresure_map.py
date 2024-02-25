line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print("Where do you want to put the treasure?")
position = input()
position = position.upper()

first_position = position[0]
second_position = int(position[1] )

i = 0
j = 0
   
if first_position == "A":  
    i = 0
elif first_position == "B": 
    i = 1
elif first_position == "C": 
    i = 2

if second_position == 1: 
    j = 0
elif second_position == 2: 
    j = 1
elif second_position == 3: 
    j = 2

map[j][i] = "X"

print(f"{line1}\n{line2}\n{line3}")
