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

# Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers.
# Also sets do not allow duplicate values.
# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set

#example of empty sets:

empty_set = {} #this is wrong because it'll be considered as a dictionary
print(type(empty_set))

empty_set2 = set() #this is correct
print(type(empty_set2)) 

#Joining Sets
# Sets in python more or less work in the same way as sets in mathematics.
# We can perform operations like union and intersection on the sets just like in mathematics.

# I. union() and update():
# The union() and update() methods prints all items that are present in the two sets.
# The union() method returns a new set whereas update() method adds item into the existing set from another set.

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))

s1.update(s2)
print(s1, s2)

#II. intersection and intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets.
# The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities. intersection(cities2)
print(cities3)

cities = ("Tokyo", "Madrid", "Berlin", "Delht")
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.Intersection_update(cities2) 
print(cities)

# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
# The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities)

# IV. difference() and difference_update():
# The difference() and difference update() methods prints only items that are only present in the original set and not in both the sets.
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

cittes = {"Tokyo", "Madrid", "Berlin", "Delht"}
cities3 = cities.difference(cities2)
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities3)

#SET METHODS:
# There are several in-built methods used for the manipulation of set. They are explained below
# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set.
# It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset (cities2))

cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset (cities3))

#issubset():
# The issubset() method checks if all the items of the original set are present in the particular set.
# It returns True if all the items are present, else it returns False.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cittes2 = {"Delhi", "Madrid"} 
print(cities2.issubset (cities))

#add()
# If you want to add a single item to the set use the add() method.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki") 
print(cities)

# update()
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary),
# and use the update() method to add it into the existing set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# remove()/discard():
# We can use remove() and discard() methods to remove items form list

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# The main difference between remove and discard is that,
# if we try to delete an item which is not present in set, then remove) raises an error, whereas discard) does not raise any error.

cities = {"Tokyo", "Madrid", "Berlis", "Dell"}
print(cities)
cities.remove(seoul)