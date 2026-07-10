#continue or break statements:
#BREAK Statement:the break statement enables a program to skip over a part of code. A break statement terminates the very loop it lies within.
#CONTINUE statement: the continue statement skips the rest of the loop statements and causes the next iteration to occur.

from ast import While


print("Break statement:")

print("example 1:")
for i in range(10): #for loops
    if i+1 == 5:
        break
    print(i+1)

print("example 2:")

i = 0
while i <= 10: #while loops
    if i+1 == 5:
        break
    print("5 X", i+1, "=", 5*(i+1))
    i += 1


print("Continue statement:")

print("example 1:")
for i in range(10):  #for loops
    if i == 5: #it'll skip 5
        continue
    print(i)

print("example 2:")
i = 0
while i < 10:  #while loops
    if i+1 == 5:
        i += 1
        continue
    print("5 X", i+1, "=", 5*(i+1))
    i += 1


#Do While loop in python:

#do while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and 
#then the repetition of loop's body will depend on the condition passed at the end of the while loop.
#It is also known as an exit-controlled loop.

# OR do while loop first executes the code block and then checks the condition, whereas a while loop first checks the condition and then executes the code block.
#This means that a do while loop will always execute at least once, even if the condition is false from the beginning,
#while a while loop may not execute at all if the condition is false.

#How to emulate a do while loop in python:
#To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.
#The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement
#that checks a given condition and breaks the iteration if that condition becomes true:

print("example 1:")

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break

print("example 2:")
while True:          # Start an endless loop
    print("Hello!")  # Do the thing FIRST
    x = int(input("Enter a number: "))

    if x <= 0:       # Check the condition
        break        # Stop if condition is met

print("example 3:")

while True:
    age = int(input("Enter your age: "))
    
    if age > 0:
        print(f"Thanks Brynex, your age {age} is valid!")
        break
    else:
        print("Invalid age, try again.")

# this programm will first print "Hello!" and then ask the user to enter a number.
# If the user enters a number less than or equal to 0, the loop will break and the program will end.
# Otherwise, if you enter any number greater than 0, then it will continue to print "Hello!" and ask for a number again.


