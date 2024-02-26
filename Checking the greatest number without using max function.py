# Checking the greatest number without using max function

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
number3 = float(input("Enter your third number: "))

if ( number1 > number2 ) and ( number1 > number3 ) :
    print(f"The first number that is {number1} is greatest.")

elif ( number2 > number3) :
    print(f"The first number that is {number2} is greatest.")
    
else: 
    print(f"The first number that is {number3} is greatest.")
