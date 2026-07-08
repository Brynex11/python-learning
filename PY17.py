# PYTHON SETS:
# Sets are unordered collection of data items. They store multiple items in a single variable. 
# Set items are separated by commas and enclosed within curly brackets {}.
# Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

#example:

info = {"Carla", 19, False, 5.9, 19} #it's output will may or may not be the same everytime when you will run the program.
print(info)

#example:

num = {2, 3, 4, 2, 2}
print(num)

#example of empty sets:

empty_set = {} #this is wrong because it'll be considered as a dictionary
print(type(empty_set))

empty_set2 = set() #this is correct
print(type(empty_set2))
