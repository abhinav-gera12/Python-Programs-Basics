# using anonymous function find the power of the given number

number = int(input("Enter the number:  "))

nterms = int(input(f"enter the powers rasied to {number} : "))
if nterms == 0:
    print(1)
else:
    result = list(map(lambda x: number ** x, range(0,nterms+1)))
    print(result)
    for i in range(1,nterms+1):
        print(f"The value of {number} raised to the power {i} is {result[i]}")