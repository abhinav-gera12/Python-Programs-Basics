# Printing prime numbers from a particular range 
# taking range from 1 to 100
lower = 1
upper = 100
for number in range (lower, upper+1):
    if number > 1:
        for i in range (2,number):
            if number % i == 0:
                break
        else:
            print(number)