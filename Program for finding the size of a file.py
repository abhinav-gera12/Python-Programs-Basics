#Program for finding the size of a file
import os 

file_size = os.stat("C:/Users/abhin/Downloads/Miniconda3-latest-Windows-x86_64.exe")
print(f"The size of the file is {file_size.st_size} in bytes")
