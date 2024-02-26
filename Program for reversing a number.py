#Program for reversing a number

number = int(input("Enter a number here: "))
reverse = 0

while (number != 0):
    digit = number % 10
    reverse = reverse*10 + digit
    number = number // 10

print(f"the reverse of given number is : {reverse}")