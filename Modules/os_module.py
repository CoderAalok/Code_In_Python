# import sys
# print(dir(sys))



# os module is built-in module in python, use to operate the any file
import os
import pathlib

# print(dir(os))

# os.rename("selling.log", 'selling_items.log')

# change directory path
# os.chdir("C://")
# print(os.getcwd())

 #It check whether the file exist
# print(os.access(file, os.W_OK)) 

# Main current working directory
print((os.getcwd()))

# this give current working directory instead of main directory
base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir)

file_path = os.path.join(base_dir, "Metacharacter.txt")

if os.path.exists(file_path):
    print(True)
else:
    print(False)

print(pathlib.Path(__file__))
