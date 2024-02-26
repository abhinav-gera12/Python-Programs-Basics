# Program to convert decimal to binary, octal, and hexadecimal

decimal = int(input("Enter a number: "))
print(f"The conversion of decimal number is {decimal}")
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print(f"The value of {decimal} in binary, octal, and hexadecimal is {binary}, {octal}, {hexadecimal} respectively.")