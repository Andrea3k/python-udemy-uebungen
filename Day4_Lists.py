# Lists - for Datastructure
# grouped pieces of data (relationships in between e.g. all states of america)
# data that is sorted/in a special order (people wainting in a queue)
# square brackets
# fruits = [item1, item2, ...]
# docs.python.org --> documentation --> hier m

states_of_america = ["Delaware", "Hawaii", ]

# Abfrage von Elementen aus der Liste über die Position in der Liste, beginnend mit 0
states_of_america [0]

# der letzte Eintrag mit -1
states_of_america [-1]

# den Eintrag an einer bestimmten Stelle überschreiben/ändern
states_of_america [1] = "xxxxx"
states_of_america.extend (["sssss", "dddd"])

# nested lists
fruits = []
vegetables= []
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)