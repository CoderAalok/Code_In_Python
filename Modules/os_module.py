# os module is built-in module in python, use to operate the any file

# import os

# print(dir(os))
# os.rename("selling.log", 'selling_items.log')
# current working directory
# print((os.getcwd()))
# os.chdir("C://")
# print(os.getcwd())

import os
import logging
import re

logging.basicConfig(filename="filename.log",
        level=logging.WARNING,
        format=('%(levelname)s:%(asctime)s:%(message)s')
    )

def extention(ext):
    files = os.listdir()
    number = []
    pattern = re.compile(r'^(\d{2})') 
    
    for file in files:
        name, ext_n = os.path.splitext(file)
        match = pattern.match(name)
        if ext_n == f".{ext}" and match:
            # count no. of ext file
            number.append(int(match.group(1)))
            
    start = max(number) + 1 if number else 1
    
    for file1 in files:
        file_name, ext_name = os.path.splitext(file1)
        
        if ext_name == f".{ext}" and not pattern.match(file_name):
            new_file_name = f"{start:02}_{file_name}{ext_name}"
            os.rename(file1, new_file_name)
            logging.warning(f"{file1} -> Successfully name changed.")
            start += 1
                
ext = input("Enter your file extention: ").replace(" ","").strip('.').lower()

if ext in ['jpg', 'log', 'py', 'pkl']:
    extention(ext)
    print("Done")
else:
    print("Sorry! I cannot changed your file name.")

