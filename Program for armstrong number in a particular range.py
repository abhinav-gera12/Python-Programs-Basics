#Program for armstrong number in a particular range (100,1000)

for number in range(100,1000):
    length = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        new_digit = digit ** length
        sum = sum + new_digit
        temp = temp//10
    if number == sum:
        print(number)
    else:
        pass
