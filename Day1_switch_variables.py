# switch variables
a = input("Insert first number here: ")
b = input("Insert second number here: ")
c = a 
a = b 
b = c 
print(a) 
print(b)


# Lifehack: das obere kann Python auch so 
a, b = b, a 
