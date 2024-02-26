#Program for creating a dictionary while using two lists

name = ["Bharat","Arun","Akshita","Abhinav"]
marks = [78,89,45,56]

dictionary = zip(name, marks)

print(dict(dictionary))