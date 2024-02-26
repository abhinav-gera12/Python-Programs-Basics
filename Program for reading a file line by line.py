#Program for reading a file line by line
import os

f = open("C:/Users/abhin/OneDrive/Desktop/123.txt","r")
lines = f.readlines()

print(lines)

new_lines = [x.strip() for x in lines]      #removing \n from the output
print(new_lines)
f.close()