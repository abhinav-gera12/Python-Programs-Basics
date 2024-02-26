#Program to check the Armstrong number

number = int(input("Enter a number for checking the armstrong number: "))
length= len(str(number)) #we can't calculate the length of an int value so we have to convert that into the string first and then gets the actual length of the number.

sum = 0
temp = number           # creating a temporary variable so that we can make changes on the temporary number
while temp > 0:       
    digit = temp%10      #capturing the last digit from the reminder
    sum += digit**length    #then, we are multiplying the number according to the length of the given number.
    temp = temp//10         #for capturing the next digit from the given number by using the floor division method.
    
if sum == number:           #if the sum is equal to the number then the coditions
    print("It is an armstrong number.")
else: 
    print("It is not an armstrong number.")