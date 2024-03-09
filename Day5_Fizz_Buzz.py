for n in range(1, 101): 
    if n % 3 == 0 and n % 5 == 0: 
        print("FizzBuzz")
    elif n % 3 == 0: 
        print("Fizz")
    elif n % 5 == 0: 
        print("Buzz")
    else: 
        print(n)


# oder so: 

# for num in range(1, 101): 
#     text = ""
#     if num % 3 == 0:
#         text += "Fizz"
#     if num % 5 == 0:
#         text += "Buzz"
#     if text = "":
#         print(num)
#     else: 
#         print(text)