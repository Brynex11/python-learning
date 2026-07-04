#PYTHON LISTS:
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation

from itertools import count


print("example 1:\n")
Lst1 = [1, 2, 3, 4, 5]
Lst2 = [2, 3, "hello", "brynex", True, 3.14]

print(Lst1)
print(Lst2)

#List index:
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list.
# The first item has index [0], second item has index [1], third item has index [2] and so on

#Accessing list items:
#We can access list items by using its index with the square bracket syntax [].

print("example 2:\n")

print(Lst2[0])  # Accessing the first item of the list #NOTE: Positive indexing starts from 0,1,2,3....
print(Lst2[3])  # Accessing the fourth item of the list

print(Lst2[-1])  # Accessing the last item of the list #NOTE: Negative indexing starts from -1,-2,-3,-4....
print(Lst2[-3])  # Accessing the third last item of the list

#Trick to find the item via positive indexing when they are in negative index:
print("example 3:\n")

print(Lst2[len(Lst2) - 3])  # Accessing the third last item of the list via positive indexing 
print(Lst2[6-3]) 

if 3.14 in Lst2:
    print("yes")
else:
    print("no")

#Range of Index:
#You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.
# Syntax:
# listName[start, end, jumpIndex]
# NOTE: jump Index is optional. We will see this in later examples

animals = ["cat", "dog", "rabbit", "parrot", "fish", "tiger", "lion"]

print(animals)  
print(animals[0:7])  # prints the items from index 0 to index 6 (7 is excluded)
print(animals[1:7:2])  # prints the items from index 1 to index 6 with a jump of 2 indexes
print(animals[1:-1])  # prints the items from index 1 to index -2 (last item is excluded)

#Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.
#NOTE: The element of the end index provided will not be included.

# List Comprehension:

# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# Syntax:
# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter "o" in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_0 = [item for item in names if len(item) > 4]
print(namesWith_0)

# Example 3:

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

#LIST METHODS:

#1. list.sort()
#This method sorts the list in ascending order. The original list is updated

l = [3, 1, 4, 2, 5]
l.sort()
print(l)  # Output: [1, 2, 3, 4, 5]
l.sort(reverse=True)
print(l)  # Output: [5, 4, 3, 2, 1]

#2. list.index()
#This method returns the index of the first occurrence of the list item

l = [3, 1, 4, 2, 5]
print(l.index(4))  # Output: 2

#3. List.reverse()
#This method reverses the order of the list items. The original list is updated

l = [3, 1, 4, 2, 5]
l.reverse() 
print(l)  # Output: [5, 2, 4, 1, 3]

#4. list.count()
# Returns the count of the number of items with the given value.

l = [3, 1, 4, 2, 5, 3, 3, 3]
print(l.count(3))  # Output: 4

#5. list.copy()
# Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

l = [3, 1, 4, 2, 5]
m = l.copy() #this will create a copy of the list l and store it in m without modifying the original list l
m[2] = 10
print(m)  # Output: [3, 1, 10, 2, 5]
print(l)  # Output: [3, 1, 4, 2, 5]

l = [3, 1, 4, 2, 5]
m = l  #this will create a reference of the list l and store it in m. Any changes made to m will also affect l
m[0] = 10
print(l)  # Output: [10, 1, 4, 2, 5]
print(m)  # Output: [10, 1, 4, 2, 5]

# 6. list.append():
# This method appends items to the end of the existing list

l = [3, 1, 4, 2, 5]
l.append(6) #this will add the item 6 to the end of the list l
print(l)  # Output: [3, 1, 4, 2, 5, 6]

# 7. list.extend():
# This method adds multiple items to the end of the existing list
l = [3, 1, 4, 2, 5]
l.extend([6, 7, 8]) #this will add the items 6, 7, and 8 to the end of the list l
print(l)  # Output: [3, 1, 4, 2, 5, 6, 7, 8]

# 8. list.insert():
# This method inserts an item at the given index. User has to specify index. and the item to be inserted within the insert() method.
l = [3, 1, 4, 2, 5]
l.insert(2, 10) #this will insert the item 10 at index 2 of the list l
print(l)  # Output: [3, 1, 10, 4, 2, 5]

# 9. Concatenating two lists:
# You can simply concatenate two lists to join two lists. 

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1 + l2)  # Output: [1, 2, 3, 4, 5, 6]

K = [1, "hello", "world", "hello"]

print(K.index("hello"))  # Output: 1. this tells the index of the first occurrence of the item "hello" in the list K

print(K.count("hello"))  # Output: 2. this tells the count of the number of items with the value "hello" in the list K

#10. list.remove():
# This method removes the first occurrence of the specified item from the list.

l = [3, 1, 4, 2, 5, 3]
l.remove(3) #this will remove the first occurrence of the item 3 from the list l
print(l)  # Output: [1, 4, 2, 5, 3]

#11. list.pop():
# This method removes the item at the specified index and returns it. If no index is specified, it removes and returns the last item in the list.

l = [3, 1, 4, 2, 5]
print(l.pop())  # Output: 5. this will remove and return the last item
print(l)  # Output: [3, 1, 4, 2]

k = l.pop(2)  # this will remove and return the item at index 2
print(k)  # Output: 4
print(l)  # Output: [3, 1, 2]
