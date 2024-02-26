#Check the number is prime or not

n = int(input("Enter the number: "))

if n <= 1:
    print(f"{n}It is not a prime number.")

if n > 1:
    for i in range(2,n):
        if n % i == 0 :
            print(f"{n}  is not prime")
            break
    else:
        print(f"{n} is a prime number")