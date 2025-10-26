a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    result = a + b
    print(f"The sum of {a} and {b} is {result}")        
elif operation == "-":
    result = a - b
    print(f"The difference of {a} and {b} is {result}")
elif operation == "*":
    result = a * b
    print(f"The product of {a} and {b} is {result}")
elif operation == "/":
    if b != 0:
        result = a / b
        print(f"The division of {a} by {b} is {result}")
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print("Invalid operation selected.")