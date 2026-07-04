#FUNCTIONS IN PYTHON
# A function is a block of code that performs a specific task whenever it is called.
# In bigger programs, where we have large amounts of code, 
# it is advisable to create or use existing functions that make the program flow organized and neat.

#There are two types of functions in Python:
#1.BUILT IN FUNCTIONS:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
# min(), max(), len(), sum(0), type(), range(), dict(), list(), tuple(), set(), print(), etc.

#2. USER DEFINED FUNCTIONS:
#We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions

print("to find geometric mean of two numbers:")

a = int(input("Enter first number(integer): "))
b = int(input("Enter second number(integer): "))

geometric_mean = (a * b)/(a + b)  # formula for geometric mean

print("Geometric mean of", a, "and", b, "is:", geometric_mean)

print("This is the way to find geometric mean without using user-defined function, \n now we will see how to do it using user-defined function")

print("to find geometric mean of two numbers using user-defined function:")

def geometric_mean(a, b):
    return (a * b) / (a + b)

a = int(input("Enter first number(integer): "))
b = int(input("Enter second number(integer): "))

print("Geometric mean of", a, "and", b, "is:", geometric_mean(a, b))

# we don't need to write the formula again and again,
# we can just call the function and pass the values to it. This makes our code more organized and neat.

print("Now we will see how can we use different varibles to find \n without writing the same function again and again:")

c = float(input("Enter first number(float): "))
d = float(input("Enter second number(float): "))

print("Geometric mean of", c, "and", d, "is:", geometric_mean(c, d))

# sometimes we may want to complete the function later,
# so to not get error in the code we use "pass" in the indent block of the user-defined function.
# This will not give any error and we can complete the function later.

def incomplete_function():
    pass  # This is a placeholder for future code

# calling a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

print("calling a function:")

def greet(first_name, last_name):
    print("Hello,", first_name, last_name + "!")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
greet(first_name, last_name)  # calling the function with user input

# FUNCTIONS, ARGUMENTS AND RETURN STATEMENTS:
# There are four types of arguments that we can provide in a function:
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable length Arguments
# 4. Required Arguments

# Default arguments:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.
# print("Default arguments example 1:")

def greet(fname = "Madhur" , mname = "Kishore" , lmname = "Dhiman"):
    print("Hello,", fname, mname, lmname + "!")

#here Madhur, Kishore and Dhiman are default arguments.

greet(fname = "John")
greet(fname= "Jane", mname = "Doe")
greet(fname = "Alice", mname = "Bob", lmname = "Smith")

#Keyword arguments:
#We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name.
# Hence, the the order in which the arguments are passed does not matter.

print("Keyword arguments example 1:")

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname + "!")

name(lname = "Dhiman", fname = "Madhur", mname = "Kishore")  # order does not matter

#REQUIRED ARGUMENTS:
# In case we don't pass the arguments with a key = value syntax, 
# then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# Example 1: when number of arguments passed does not match to the actual function definition

print("Required arguments example 1:")

def required_args(fname, mname, lname):
    print("Hello,", fname, mname, lname + "!")

# required_args("Madhur", "Kishore")  # This will cause an error as not all required arguments are provided
required_args("Madhur", "Kishore", "Dhiman")  # This will work correctly

#VARIABLE LENGTH ARGUMENTS:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.
# There are two ways to achieve this:

# 1. Arbitrary Arguments:
# While creating a function, pass a before the parameter name while defining the function.
# The function accesses the arguments by processing them in the form of tuple.

def name(*name):
    print("Hello", name[0], name[1], name[2]) 
#the numbers in the square brackets represent indexing of the tuple because in python counting starts from 0,1,2....

name("James", "Buchanan", "Barnes")

# # 2. Keyword Arbitrary Arguments:
# # While creating a function, pass a before the parameter name while defining the function.
# # The function accesses the arguments by processing them in the form of dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#NOTE: 
# * and ** in Python Functions

# * (single star) — for POSITIONAL arguments
# - Used in function definition: def func(*args)
# - Collects any number of positional arguments into a TUPLE
# - Example:
def average(*numbers):
        print(numbers)

average(5, 6, 7)   # numbers = (5, 6, 7)

# - Also used to UNPACK a list/tuple into separate arguments when calling a function:
my_list = [10, 20, 30]
average(*my_list)   # sends 10, 20, 30 as separate args


# ** (double star) — for KEYWORD arguments
# - Used in function definition: def func(**kwargs)
# - Collects any number of keyword (named) arguments into a DICTIONARY
# - Example:
def name(**info):
        print(info["fname"], info["lname"])

name(fname="James", lname="Barnes")

# - Also used to UNPACK a dictionary into keyword arguments when calling a function:
my_dict = {"fname": "James", "lname": "Barnes"}
name(**my_dict)


# Quick Rule:
# - *  → positional values → tuple
# - ** → keyword values    → dictionary
# - No such thing as *** in Python
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def average(*numbers):
    sum = 0
    for i in numbers:
         sum = sum + i
    return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)   






