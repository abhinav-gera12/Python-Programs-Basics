# Program for multiplication table using while loop

number = int(input("enter the number to see the multiplication table: "))
i = 1
while i <= 10:
    result = number * i
    print(f"{number} * {i} = {result}")
    i = i + 1