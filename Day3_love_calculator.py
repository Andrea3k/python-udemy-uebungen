print("The Love Calculator is calculating your score...")
name_1 = input("What is the first name?\n")
name_2 = input("What is the second name?\n")
name = name_1.lower() + name_2.lower()
t,r,u,e = 0,0,0,0
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
total_1 = t + r + u + e
l,o,v,e = 0,0,0,0
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
total_2 = l + o + v + e
love_score = str(total_1) + str(total_2)
love_score = int(love_score)
if love_score < 10 or love_score > 90: 
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50: 
    print(f"Your score is {love_score}, you are alright together")
else: 
    print(f"Your score is {love_score}")

# Rebecca Lösung ist smoother: 

# count_true = 0
# count_love = 0
    
# count_true += count_true.count("t")
# count_true += count_true.count("r")
# count_true += count_true.count("u")
# count_true += count_true.count("e")
    
# count_love += count_love.count("l")
# count_love += count_love.count("o")
# count_love += count_love.count("v")
# count_love += count_love.count("e")