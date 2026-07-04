#Match case statements:

#To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language,
#you must have heard of switch-case statements. If this is your first language, DW.

#A match statement will compare a given variable's value to different shapes, also referred to as the pattern.
#The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

# The match case consists of three main entities:
# 1. The match keyword
# 2. One or more case clausesThe case clause consists of a pattern to be matched to the variable,
# 3. Expression for each case
#  a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches
#Example of a match case statement


giveaway = int(input("enter a number between 1 to 10 (integers only): "))
match giveaway:

    case 1:
        print("you have won a car!")
    case 2:
        print("you have won a bike!")
    case 3:
        print("you have won a laptop!")
    case 4:
        print("you have won a smartphone!")
    case 5:
        print("you have won a tablet!")
    case 6:
        print("you have won a smartwatch!")
    case 7:
        print("you have won a gaming console!")
    case 8:
        print("you have won a gift card worth $100!")
    case 9:
        print("you have won a vacation package!")
    case 10:
        print("you have won a home theater system!")
    case _: #the underscore (_) is a wildcard/default pattern that matches anything. It is used as a catch-all case to handle any values that do not match the specified cases.
        print("invalid input! please enter a number between 1 to 10 only")