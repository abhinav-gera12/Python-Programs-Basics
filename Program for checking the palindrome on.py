# Program for checking the palindrome on a string
string = input("Enter a string to check: ")
string = string.lower()
reverse = string[ : :-1]
reverse = reverse.lower()
if string == reverse:
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")