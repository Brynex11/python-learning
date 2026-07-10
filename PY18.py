# Python Dictionaries
# Dictionaries are ordered collection of data items. They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets ().

dic = {  "Harry":"Human being",
"Spoon":"Object"
}

print(dic["Harry"])
print(dic["Spoon"])
print(dic)

# Accessing Dictionary items:

# I. Accessing single values:
# Values in a dictionary can be accessed using keys. 
# We can access dictionary values by mentioning keys either in square brackets or by using eet method.

info = {'name': 'Karan', 'age':19, 'eligible': True}
print(info)
print(info['name'])
print(info.get('name'))

# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.

info = {"name" : Brynex , "age" : 19 , "eligible" : True}
print(info)
print(info.values())


# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method

info = {'name': 'Karan', 'age': 119, 'eligible': True}
print(info.keys())

for key in info.keys():
    print(info[key])

for key in info.keys():
 print(f"The value corresponding to the key {key} is {info[key]}")

# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method

info = {'name': 'Karan', 'age': 119, 'eligible': True}

print(info.items())

for key, value in info.items():
   print(f"The value corresponding to the key {key} is {value}")