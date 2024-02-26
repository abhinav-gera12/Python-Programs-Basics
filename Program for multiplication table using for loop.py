# Program for multiplication table using for loop

number = int(input("enter the number to see the multiplication table: "))
for i in range(1,11):
    result = number * i
    print(f"{number} * {i} = {result}")
    i = i + 1