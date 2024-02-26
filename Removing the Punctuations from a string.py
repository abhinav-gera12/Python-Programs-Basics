#Program for removing the punctuations from a string

string = input("Enter a string: ")
empty_string = ""

punctuations = """!@#$%^&*()-_=+[{]}\|'";:/?.>,<`~]""" 
#don't add spaces otherwise it takes spaces as a punctuation.

for i in string:
    if i not in punctuations:
        empty_string = empty_string + i
    
print(empty_string)