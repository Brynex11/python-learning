#MANIPULATING TUPLES IN PYTHON
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list.
# Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia") #add item
temp.pop(3) #remove item at index 3
temp[2] = "Finland" #change item at index 2
countries =  tuple(temp)
print(countries)

# Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.
# However, we can directly concatenate two tuples without converting them to list

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka") 
countries2 = ("Vietnam", "India", "China") 
southEastAsia = countries + countries2
print(southEastAsia)

#Tuple methods
# As tuple is immutable type of collection of elements it have limited built in methods. They are explained below.

# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:', res)

#index() Method
# The index() method of Tuple returns the index of the first occurrence of the given element in

kes = tuple1.index(2, 4, 7) #this will return the index of the first occurrence of the item 2 in the tuple tuple1 between index 4 and 7
print('Index of 2 in tuple1 between index 4 and 7 is:', kes)

