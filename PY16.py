#RECURSION IN PYTHON: 
# Recursion is the process of defining something in terms of itself
# A physical world example would be to place two parallel mirrors facing each other. 
# Any object in between them would be reflected recursively

#PYHTON RECURSION FUNCTION:
# In Python, we know that a function can call other functions.
# It is even possible for the function to call itself.
# These types of construct are termed as recursive functions

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return (num*factorial(num-1))
    
# Driver Code
num = 7;
print("Number: ", num)
print("Factorial: ", factorial(num))