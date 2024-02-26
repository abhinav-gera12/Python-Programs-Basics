# finding the factorial of given number using recursion function
# recursion is the function which call itself as a function.

def factorial(number):
    if number == 0:
        return 1
    else:
        return ((number) * factorial(number-1))     #using recursion method
    
number = int(input("Enter the number for factorial calculation: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")