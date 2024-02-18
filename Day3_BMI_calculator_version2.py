# BMI calculator 
height = 1.75
weight = 78 
BMI = weight/height**2
round(BMI,2)
print(f"Your BMI is {BMI}")
if BMI < 18.5: 
    print("You are underweight!")
elif BMI < 25:
    print("You have a normal weight")
elif BMI < 30:
    print("You are slightly overweight")
elif BMI < 35:
    print("You are obese")
else: 
    print("You are clinically obese")