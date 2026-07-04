# INTRODUCTION TO LOOPS IN PYTHON
# A loop is a programming construct that allows you to repeat a block of code multiple times.
# In Python, there are two main types of loops: for loops and while loops.
#1. for loops
# A for loop is used to iterate over a sequence (like a list, tuple, string, etc.) and execute a block of code for each item in the sequence.

print("1. Iterating over a string")

colour = "green"
for x in colour:
    print(x)  # This will print each character in the string "green" on a new line

print("2. Iterating over a list")
colours = ["red", "green", "blue"]
for colour in colours:
    print(colour)  # This will print each colour in the list on a new line

print("3. Range")

# The range() function is used to generate a sequence of numbers. It can take one, two, or three arguments: start, stop, and step.
# If you provide one argument, it will be treated as the stop value, and the start will default to 0. If you provide two arguments, the first will be the start value and the second will be the stop value. If you provide three arguments, the first will be the start value, the second will be the stop value, and the third will be the step value.
for i in range(10):
    print(i)  # This will print numbers from 0 to 9 (10 is not included)

print("using specific range in for loops")

for x in range(1,11):
    print(x)  # This will print numbers from 1 to 10 (11 is not included)

print("using arithmetic progression using specific range in for loops")

#range(start, stop, step)

for y in range(1,12,3):   #you can't add more than 3 arguments
    print(y) 


print("2. while loops:")
# While loops execute statements while the condition is true. As soon as the condition becomes false, the interpreter comes out to the while loop.
i = 0
while i <= 5: #incrementing while loop
    print(i)
    i += 1

l = 0
while l <= 50:
    l = int(input("Enter a number: "))
    print("You entered:", l)

print("3. decrementing while loop:")   
    
count = 5
while count > 0: #decrementing while loop
    print(count)
    count = count - 1

print("Else in while loop:")
# The else block in a while loop is executed when the loop condition becomes false. It is not executed if the loop is terminated by a break statement.
d = 10 
while d > 0:
    print(d)
    d -= 1
else:
    print("The loop has ended.")

















        
        
    