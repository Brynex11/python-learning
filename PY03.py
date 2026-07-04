a = 10
b = 5
sum = a + b
diff = a - b
product = a * b
division = a / b

print("Sum:", sum)
print("Difference:", diff)  
print("Product:", product)
print("Division:", division)

#type casting: implicit and explicit
#implicit type casting: when the interpreter(python) automatically converts one data type to another
#explicit type casting: when the programmer manually converts one data type to another using built-in functions like int(), float(), str(), etc.

#implicit type casting
x = 5   # integer
y = 2.0 # float
print(x + y) # Output: 7.0 (x is implicitly converted to float to prevent data loss)

#explicit type casting 
q = "3" #float(str)
w = "4" #intege(str)

print(q + w) # Output: 34 (q and w are treated as strings and concatenated)
print(int(q) + int(w)) # Output: 7 (q and w are explicitly converted to integers by using "int()" before addition)