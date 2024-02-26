# Program for calculating the highest common factor

def highest_factor(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if x % i == 0 and y % i == 0:
            HCF = i
    return HCF

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(int(highest_factor(x,y)))