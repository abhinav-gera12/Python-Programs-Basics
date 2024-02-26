# Program for Fibonacci series using recursion

def fib(n):
    if n <= 1:
        return n
    else:
        fibonacci = fib(n-1) + fib(n-2)         #n is equal the nth term # recursion method calling function itself.
        return fibonacci
n = int(input("Enter a number to print the sequence: "))
if n <= 0 :
    print("enter a positive number.")
else:
    print("Fibonaaci Series")
    for i in range(0,n):
        print(fib(i))