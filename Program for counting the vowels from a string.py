#Program for counting the vowels from a string
 
user_input = input("enter your statement: ")
vowels = "aeiou"
user_input = user_input.lower()

count = {}.fromkeys(vowels,0)

for character in user_input:
    if character in count:
        count[character] = count[character] + 1
        
print(count)