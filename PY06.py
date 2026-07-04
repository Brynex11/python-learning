#1. accessing characters in a string
 # The index starts from 0 for the first character, 1 for the second character,
#  and so on. We can also use negative indexing to access characters from the end of the string, where -1 is the last character,
#  -2 is the second last character, and so on.
name = "brynex"
print(name[0])  # Output: b
print(name[1])  # Output: r
print(name[-1])  # Output: x
print(name[-2])  # Output: e
print(name[-6] + "\n")  # Output: b (since -6 is the same as 0 in this case)

print("let us look at the string loop for characters\n")

#2. looping through a string
#if we have a paragraph of text and we want to count the number of times a specific word appears in it,
#  we can use a loop to iterate through the string and count the occurrences of the word.
paragraph = "Python is a great programming language. I love learning Python."

for character in paragraph:
    print(character)  # This will print each character in the paragraph on a new line

#NOTE : The Structure of a for Loop
# A string loop in Python always follows this structure:
# for <variable_name> in <string_to_loop_through>:

#3. length of a string
#we can use the built-in len() function to get the length of a string, which counts the number of characters in the string, including spaces and punctuation.

my_string = "Hello, World!"
length = len(my_string) # Output: 13 (including the comma and space)
print("Length of the string:", length)
# or we can do this too:

print(len(my_string)) # Output: 13 (including the comma and space)

#5.upper() and lower() methods
#the upper() method converts all characters in a string to uppercase,
#while the lower() method converts all characters to lowercase.
#note: strings are immutable, which means that these methods do not change the original string but return a new string with the desired case conversion.

text1 = "Python Programming"
text2 = "PYTHON PROGRAMMING"

print(text1.upper() + "\n")  # Output: PYTHON PROGRAMMING
print(text2.lower()) # Output: python programming

#6. rstrip() and lstrip() methods
#the rstrip() method removes any trailing whitespace characters from the right end of a string, while the lstrip() method removes any leading whitespace characters from the left end of a string.
#note: these methods do not change the original string but return a new string with the whitespace

text3 = "!!!!brynex!!!!"

print(text3.rstrip("!"))  # Output: !!!!brynex
print(text3.lstrip("!"))  # Output: brynex!!!!

#7. replace() method
#the replace() method is used to replace occurrences of a specified substring with another substring in a string.

text4 = "I like Python programming. Python is great!"
new_text = text4.replace("Python", "Java")
print(new_text)  # Output: I like Java programming. Java is great!

#or we can also do this:

print(text4.replace("Python", "C++"))  # Output: I like C++ programming. C++ is great!

#8. split() method
#the split() method is used to split a string into a list of substrings. 

text5 = "Hello, how are you doing today? I hope you are doing well."

print(text5.split())  # Output: ['Hello,', 'how', 'are', 'you', 'doing', 'today?', 'I', 'hope', 'you', 'are', 'doing', 'well.']

#9  . capitalize() method
#the capitalize() method converts the first character of a string to uppercase and the rest to lowercase. It has no effect on already capitalized characters or non-alphabetic characters.
#this also corrects the case of the rest of the characters in the string, making them lowercase.
text6 = "hello, my name is bryNex. i am lEarNing python."
print(text6.capitalize())  # Output: Hello, my name is brynex. i am learning python.

#10. center() method
#the center() method is used to center-align a string within a specified width. It takes the width as an argument and returns a new string that is centered within that width, with padding added on both sides if necessary.
text7 = "Python"
print(text7.center(10))  # Output:   Python   

#11. count() method
#the count() method is used to count the number of occurrences of a specified substring in a string.
text8 = "Hello, how are you doing today? I hope you are doing well."
print(text8.count("you"))  # Output: 2
print(text8.count("doing"))  # Output: 2

#12. endswith() method
#the endswith() method is used to check if a string ends with a specified suffix. It returns True if the string ends with the specified suffix, and False otherwise.
# the endswith() method can also take an optional start and end parameter to specify a range within the string to check for the suffix. If the start and end parameters are not provided, the method checks the entire string.
text9 = "Hello, how are you doing today? I hope you are doing well."    
print(text9.endswith("well."))  # Output: True
print(text9.endswith("today?"))  # Output: False    

print(text9.endswith("doing", 0, 30))  # Output: False (checks if the substring "doing" is at the end of the specified range)
print(text9.endswith("you", 0, 18))  # Output: True (checks if the substring "you" is at the end of the specified range)

#13. find() method
#the find() method is used to find the index of the first occurrence of a specified substring in a string. It returns the index of the first occurrence of the substring, or -1 if the substring is not found.
text10 = "Hello, how are you doing today? I hope you are doing well."
print(text10.find("you"))  # Output: 15 (the index of the first occurrence of "you")
print(text10.find("hussle"))  # Output: -1 (since "hussle" is not found in the string)

#14. index() method
#the index() method is similar to the find() method, but it raises a ValueError if the specified substring is not found in the string, instead of returning -1.
text11 = "Hello, how are you doing today? I hope you are doing well."
print(text11.index("you"))  # Output: 15 (the index of the first occurrence of "you")


#15. isalpha() method
#the isalpha() method is used to check if all characters in a string are alphabetic. It returns True if all characters are alphabetic and there is at least one character, and False otherwise.

text12 = "Hello"
text13 = "Hello123"

print(text12.isalpha())  # Output: True (all characters are alphabetic)
print(text13.isalpha())  # Output: False (contains non-alphabetic characters)
 
#16. isalnum() method
#the isalnum() method is used to check if all characters in a string are alphanumeric (i.e., letters and numbers). It returns True if all characters are alphanumeric and there is at least one character, and False otherwise.
text14 = "Hello123"
text15 = "Hello 123" 

print(text14.isalnum())  # Output: True (all characters are alphanumeric)
print(text15.isalnum())  # Output: False (contains a space, which is not alphanumeric)

#17. islower() method
#the islower() method is used to check if all characters in a string are lowercase. It returns True if all characters are lowercase and there is at least one character, and False otherwise.

text16 = "hello"
text17 = "Hello"

print(text16.islower())  # Output: True (all characters are lowercase)
print(text17.islower())  # Output: False (contains an uppercase character)

#18. isprintible() method
#the isprintable() method is used to check if all characters in a string are printable. It returns True if all characters are printable and there is at least one character, and False otherwise.

text18 = "Hello, World!"
text19 = "Hello\nWorld" 

print(text19)

print(text18.isprintable())  # Output: True (all characters are printable)
print(text19.isprintable())  # Output: False (contains a newline character, which is not printable)

#19. isspace() method
#the isspace() method is used to check if all characters in a string are whitespace characters. It returns True if all characters are whitespace and there is at least one character, and False otherwise.
text20 = "   " #it can be using tab or space bar 
text21 = "Hello"

print(text20.isspace())  # Output: True (all characters are whitespace)
print(text21.isspace())  # Output: False (contains non-whitespace characters)

#20. istitle() method
#the istitle() method is used to check if a string is in title case. A string is considered to be in title case if the first character of each word is uppercase and the rest of the characters are lowercase. The method returns True if the string is in title case, and False otherwise.
text22 = "Hello, World!"
text23 = "hello, world!"

print(text22.istitle())  # Output: True (each word starts with an uppercase letter)
print(text23.istitle())  # Output: False (each word does not start with an uppercase letter)

#21. isupper() method
#the isupper() method is used to check if all characters in a string are uppercase. It returns True if all characters are uppercase and there is at least one character, and False otherwise.   
text24 = "HELLO"
text25 = "Hello"

print(text24.isupper())  # Output: True (all characters are uppercase)
print(text25.isupper())  # Output: False (contains a lowercase character)

#22. startswith() method
#the startswith() method is used to check if a string starts with a specified prefix. It returns True if the string starts with the specified prefix, and False otherwise.
text26 = "Hello, how are you doing today? I hope you are doing well."
print(text26.startswith("Hello"))  # Output: True (the string starts with "Hello")
print(text26.startswith("how"))    # Output: False (the string does not start with "how")


#23. swapcase() method
#the swapcase() method is used to convert all uppercase characters in a string to lowercase, and all lowercase characters to uppercase. It returns a new string with the case of each character swapped.
text27 = "Hello, World!"
print(text27.swapcase())  # Output: hELLO, wORLD!