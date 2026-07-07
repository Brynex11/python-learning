#RECURSION IN PYTHON: 
# Recursion is the process of defining something in terms of itself
# A physical world example would be to place two parallel mirrors facing each other. 
# Any object in between them would be reflected recursively

#PYHTON RECURSION FUNCTION:
# In Python, we know that a function can call other functions.
# It is even possible for the function to call itself.
# These types of construct are termed as recursive functions

def factorial(num):
    if (num == 0 or num == 1): # base case
        return 1
    else:
        return (num*factorial(num-1)) # recursive case
    
# Driver Code
num = 7;
print("Number: ", num)
print("Factorial: ", factorial(num))

# NOTE: Every recursive function needs a base case.
# Without one, the function keeps calling itself forever
# and Python eventually throws a RecursionError (stack overflow).

# FIBONACCI USING RECURSION:
# Each number is the sum of the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Driver Code
print("Fibonacci of 6:", fibonacci(6))

# RECURSION vs ITERATION:
# Both can solve repetitive problems.
# - Iteration (loops) is usually more memory-efficient.
# - Recursion is often more readable for problems that are
#   naturally defined in terms of themselves (factorial, tree traversal, etc.)
# factorial() could also be written using a simple for loop instead.