#conditional operators
# >,<,==,>=!=,,<=(note: equal to "=" is not an conditional operator, it is an assignment operator)

#Indentation in Python
# In Python, indentation refers to the empty space (leading whitespace) at the beginning of a line of code.

#Unlike many other programming languages that use curly braces { } to group blocks of code, Python uses indentation to determine the structure and hierarchy of the program.
#It tells the computer which lines of code belong together as a single block.
#The standard practice is to use four spaces for each level of indentation.

#1. if, else and elif statements
# The if statement evaluates a condition. If that condition is True, the indented block of code underneath it runs. If it's False, Python simply skips it.
#The else statement acts as a safety net. It doesn't have its own condition; instead, it catches everything that the if statement missed. It only runs if the if condition evaluates to False
# The elif statement is a combination of "else" and "if". It allows you to check multiple conditions after the initial if statement. If the first condition is False, it checks the next one, and so on.
print("JEE MAINS RESULT IS LIVE NOW! FILL IN YOUR DETAILS TO CHECK YOUR RESULT")

a = int(input(" enter your application number: "))
print("application number is:", a)

b = int(input("enter your password(integers only): "))

c = int(input("choose a number between 1 to 100: "))
print("your chosen number is:", c)

if(c==100):
    print("JEE Mains Score: 360/360")
    print("Total percentile is: 100.0000000")
    print("All India Rank is: 1")
    print("congratulations! you have qualified JEE Mains and you are eligible for JEE ADVANCED!")
    print("thank you for using our service, For JOSSA counselling portal will be live soon, stay tuned!")

elif(c>50 and c<100): #note: you can use more than one elif statements.
    print("JEE Mains Score: 200/360")
    print("Total percentile is: 99.6233234569")
    print("All India Rank is: 4159")
    print("congratulations! you have qualified JEE Mains and you are eligible for JEE ADVANCED!")
    print("thank you for using our service, For JOSSA counselling portal will be live soon, stay tuned!")

elif(c>100):
    print("invalid input! please enter a number between 1 to 100 only")
elif(c<=0):
    print("invalid input! please enter a number between 1 to 100 only")
else: 
    print("JEE Mains Score: -75/360")
    print("Total percentile is: 0.0000000")
    print("All India Rank is: 16,00,000")
    print("sorry! you have not qualified for JEE Mains")
    print("thank you for using our service, For JOSSA counselling portal will be live soon, stay tuned!")
    


