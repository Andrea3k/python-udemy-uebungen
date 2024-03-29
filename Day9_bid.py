# ask for name input
# ask for bid price
# add name and bid in dictionary as key and value
# ask if there are other users who want to bid
# clear screen
# find the highest bid in the dictionary and declare them as the winner

import os 

name = input("What is your name?: ")
bid = abs(int(input("What is your bid?: ")))
further_user = input("Are there further users?: ") # yes or no

if further_user == "yes": 
    futher_user = True
elif further_user == "no": 
    further_user = False


def add_name_bid (name, bid)
    dict_name_bid = {}
    dict_name_bid.append({
        name: bid
    })
    return dict_name_bid

dict_name_bid = add_name_bid(name, bid)

current_bid = 0
def highest_bid(): 
    for n in dict_name_bid: 
        
        if current_bid > dict_name_bid[n]
            



for users in dict_name_bid: 
    if further_user == True: 
        dict_name_bid = add_name_bid(name, bid)
        os.system('cls')
    else:
        highest_bid()

