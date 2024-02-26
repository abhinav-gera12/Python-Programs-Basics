# Find the sum of natural numbers

number = int(input("Enter the number: "))

if number < 0:
    print("Not a natural number.")
else: 
    sum = 0 
    while number > 0:
        sum = sum + number
        number = number - 1
    print(f"The sum is {sum}")
