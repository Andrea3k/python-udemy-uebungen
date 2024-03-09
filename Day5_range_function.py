# for loop with range
# in brackets: from 1 to 10 - excluding 10 - in steps of 3
for number in range(1, 10, 3): 
    print(number)


total = 0
for number in range(1,101): 
    # total = total + number
    total += number
print(total)