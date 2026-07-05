#STRING FORMATTING IN PYTHON
# String formatting can be done in python using the format method.

txt = "For only {price: .2f} dollars"
print(txt.format(price = 47.099992))

letter = "Dear {},\nYou are selected for the position of {} in our company.\nYour joining date is {}.\nThank you."
name = input("Enter your name: ")
position = input("Enter the position you are selected for: ")
joining_date = input("Enter your joining date (dd/mm/yyyy): ")

formatted_letter_1 = letter.format(name, position, joining_date) #if you were to shuffle the order of name,
# position and joining_date in the format method, it would still work as expected. 
# The order of the arguments in the format method corresponds to the order of the placeholders in the string.
print(formatted_letter_1)

formatted_letter_2 = letter.format(joining_date, position, name) #shuffled the variables in the format method,
# but the placeholders in the string remain in the same order.
print(formatted_letter_2)

letter_2 = "Dear {0},\nYou are selected for the position of {1} in our company.\nYour joining date is {2}.\nThank you."
formatted_letter_3 = letter_2.format(name, position, joining_date) #using positional arguments
# where name corresponds to {0}, position corresponds to {1}, and joining_date corresponds to {2}.
print(formatted_letter_3)

letter_3 = "Dear {name},\nYou are selected for the position of {position} in our company.\nYour joining date is {joining_date}.\nThank you."
formatted_letter_4 = letter_3.format(name=name, position=position, joining_date=joining_date) #using keyword arguments
# where name corresponds to {name}, position corresponds to {position}, and joining_date corresponds to {joining_date}.
print(formatted_letter_4)

letter_4 = "Dear {{name}},\nYou are selected for the position of {{position}} in our company.\nYour joining date is {{joining_date}}.\nThank you."
print(letter_4)

#F-STRINGS IN PYTHON

# It is a new string formatting mechanism introduced by the PEP 498.
#  It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal).
#  The primary focus of this mechanism is to make the interpolation easier=
# When we prefix the string with the letter 'f, the string becomes the f-string itself.
#  The f-string can be formatted in much same as the str.format() method.
#  The f-string offers a convenient way to embed Python expression inside string literals for formatting.

name = "Brynex"
age = 20

print(f"My name is {name} and I am {age} years old.") 

a = 5
b = 3
print(f"{a} + {b} = {a + b}")