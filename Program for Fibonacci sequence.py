# Program for Fibonacci sequence

number1 = 0
number2 = 1
number3 = int(input("Enter the number to obtain the fibonacci sequence: "))

if number3 ==1 :
    print(number1)
    
else:
    print(number1)
    print(number2)
    for i in range(2,number3):        #coz we are printing our first two numbers before the loop so the range starts from 2
        number3 = number1 + number2
        number1 = number2
        number2 = number3
        print(number3)
    