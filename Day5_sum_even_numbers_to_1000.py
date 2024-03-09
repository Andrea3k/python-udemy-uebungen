target = int(input())   # number between 0 and 1000
target = target + 1
even_sum = 0
for number in range(0,target): 
    if number % 2 == 0: 
        even_sum += number
print(even_sum)


# oder so: 

# target = int(input())   
# even_sum = 0
# for number in range(0, target + 1, 2): 
#    even_sum += number
# print(even_sum)
