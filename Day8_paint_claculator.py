import math 
def paint_calc(height, width, coverage = 5):
    number_of_cans = (height * width)/coverage
    number_of_cans = math.ceil(number_of_cans)
    return number_of_cans

height = int(input("What ist the height of your wall?"))
width = int(input("What is the Width of your wall?"))

needed_amount = paint_calc(height, width)

print(f"You need {needed_amount} cans.")