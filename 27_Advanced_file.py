#Studensts details stored....

# while True:
#     student_name = input("Enter your Name : ").capitalize()
#     if not student_name.isalpha():
#         print("Name is required.")
#         continue
#     try:
#         Roll = int(input("Enter your Roll_No. : "))
#         marks = int(input("Enter your total Marks obtaining in final board : "))
#     except ValueError:
#         print("Only valid integer type.")
     
#     with open("details.txt", 'a+')as f:
#         f.write(f"Name : {student_name} \nRoll_no. : {Roll} \nMarks : {marks} \n")
#         f.close()
    
#     add = input("Adding more (YES / NO). : ").strip().lower()
#     if not add == 'yes':
#         print("Okay! your data sucessfully stored.")
#         break

# Two in one ( two text file merges in third file)
# file1 = "file1.txt"
# file2 = "file2.txt"
# with open(file1)as f1:
#     re = f1.readline()
# with open(file2)as f2:
#     re1 = f2.readline()
# with open("file3.txt","w")as f3:
#     f3.write(re)
#     f3.write(re1)

#Alternative method ...
# file1 = "file1.txt"
# file2 = "file2.txt"  
#   
#read and write at a time
# with open(file1, 'r')as f1 , open(file2, 'r')as f2, open("file3.txt", 'w')as f3 :
#     f3.write(f"{1}. {f1.read()}")
#     f3.write("\n")
#     f3.write(f"{2}. {f2.read()}")


#Replaces all occurrences of a given word in a file with another word.

# with open("rag.txt", 'r')as f:
#     old = f.read()
#     new_word = old.replace('Mind', "The mind") # new string form by  replacing Mind .
    
# with open("rag.txt", 'w')as up:
#     up.write(new_word)
    

#CSV (Comma-Separated Values)
#📌 Why use CSV?
# ✔ Lightweight (just text)
# ✔ Easy to read/write in Excel, Google Sheets, Python, etc.
# ✔ Widely used for data exchange between applications

# import csv
# with open("info.csv", "r")as f:
#     read = csv.reader(f)
#     for i in read :
#         print(i)
    


# with open("binary.txt", "rb")as f:
#     re = f.read()
#     text = re.decode("utf-8") #It makes readable format which easly understand by human
#     # encode : data and  information make turn into binary for better understanding to the computer
#     print(text)

# with open("pi.txt", 'x+')as f:
#     print(f.read())
# 'x' create a new  file but that file already exist then error throw
# 'x+' create a new for reading and writing if the  file but that file already exist then error throw
