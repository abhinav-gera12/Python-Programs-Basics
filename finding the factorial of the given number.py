# finding the factorial of the given number

number = int(input("Enter the number: "))
factorial = 1

if number == 0:
    print("The factorial of given number is 1.")
elif number > 0:
    for i in range(1,number+1):
        factorial = factorial * i
        i = i + 1
print(f"The factorial of {number} is {factorial}")