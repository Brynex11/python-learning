print("CALCULATOR PROGRAM! After choosing 1st and 2nd numbers kindly choose an operation to proceed with the calculation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = int(input("Enter the operation number (1-4): "))

if operation == 1:
    result = a + b
    print("The result of addition is:", result)

elif operation == 2:
    result = a - b
    print("The result of subtraction is:", result)

elif operation == 3:
    result = a * b
    print("The result of multiplication is:", result)

elif operation == 4:
    if b != 0:
        result = a / b
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
print("Thank you for using the calculator program!")