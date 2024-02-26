#find all files with extension present inside a folder
import os

for files in os.listdir("C:/Users/abhin/Downloads"):
    if files.endswith(".pdf"):
        print(files) 