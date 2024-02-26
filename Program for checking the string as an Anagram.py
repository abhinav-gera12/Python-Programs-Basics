#Program for checking the string as an Anagram
#the string must be of same length
#after sorting alphabetically the string must be same just like "below" and "elbow"

a1 = "below"            #wow    #cat
a2 = "elbow"            #wow    #act 

if len(a1) == len(a2):
    a1_sort = sorted(a1)
    a2_sort = sorted(a2)
    if a1_sort == a2_sort:
        print("It is an Anagram string")
    else:
        pass
else:
    print("The string is not an Anagram")