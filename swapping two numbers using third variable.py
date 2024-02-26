#swapping two numbers using third variable
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
temp = float()

print(f"Before swapping the numbers a = {a} and b = {b}\n")

temp = a 
a = b
b = temp

print(f"After swapping the numbers a = {a} and b = {b}")