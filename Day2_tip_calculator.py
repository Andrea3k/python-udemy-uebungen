total_bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give? 10, 12 or 15\n")
amount_of_people = input("How many people to split the bill\n")
total_bill, tip, amount_of_people = float(total_bill), int(tip), int(amount_of_people)
each_person = ((total_bill*(tip/100))+total_bill)/amount_of_people
each_person = round(each_person,2)
print("Each person should pay: "+str(each_person))