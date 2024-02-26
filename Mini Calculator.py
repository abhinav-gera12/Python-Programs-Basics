# Program for calculating addition, subtraction, division and multiplication
print("\n")
print("\t\t\t\t\t\t  Mini Calculator ")

print("Press 1 for addition: ")
print("Press 2 for subtraction: ")
print("Press 3 for division: ")
print("Press 4 for multiplication:\n\n ")

user_input = float(input("Enter your choice: "))
if user_input <=4:    
    number1 = float(input("enter your first number: "))
    number2 = float(input("enter your second number: "))

    if user_input == 1:
        result = number1 + number2
        print(f"The addition of {number1} and {number2} is {result}")
        
    elif user_input == 2:
        result = number1 - number2
        print(f"The subtraction of {number1} and {number2} is {result}")
        
    elif user_input == 3:
        result = number1 / number2
        print(f"The division of {number1} and {number2} is {result}")
        
    elif user_input == 4:
        result = number1 * number2
        print(f"The multiplication of {number1} and {number2} is {result}")
        
else:
    print("Wrong Choice.")