# Dictionaries / Nesting / Lexikon
# Key - Value (Bug - an error in a program)
# {Key: Value} 
# curly braces {}
# {"Bug": "An error in a program"}
# more than one Key: Value pair --> getrennt durch , 
# array geht nicht als Key, aber man kann auch 123 nicht als string 

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
    "Loop": "The action of doing something over and over again.",
}

# retrieving items from dictionary. 
print(programming_dictionary["Bug"])

# Adding new items do dictionary
programming_dictionary["Smartphone"]="Samsung"
print(programming_dictionary)

# create an empty dictionary. 
empty_dictionary = {}

# wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# loop through a dictionary
for key in programming_dictionary: 
    print(key)
    print(programming_dictionary[key])