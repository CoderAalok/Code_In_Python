#PROBLEM 8 copy content
# with open("file1.txt", 'r')as f:
#     file1 = f.read()
# with open("file2.txt", 'w')as q:
#     file2 = q.write(file1)

# Problem 9 matching the contents...
# with open("file1.txt", 'r')as f:
#     file1 = f.read()
# with open("file2.txt", 'r')as q:
#     file2 = q.read()

# if file1 == file2 :
#      print("Identical and matches ")
# else:
#      print('Not Identical and not matches')

#problem 10 updating a file

# with open("file2.txt", '+w')as f:
#     f.write('RAG based system is too much good')
    
#problem 11 file name change...
# import os   #To changing the file name...

# old_file = "context.txt"
# new_file = 'function'
# with open(old_file)as f:
#     store = f.read()  # storing old data 
# with open(new_file , 'w')as q :
#     q.write(store)  # inputed old data
# os.remove(old_file)
# file = "log.txt"
# file1 = 'pop.txt'
# with open(file)as f :
#     q = file.replace(file,file1)
# with open(q)as f:
#     print(f.read())

# user = input("Enter your Name: ")
# with open("guest.txt",'w')as file:
    
#     file.write(user)

i = 1
while i <=3:
    user = input(f"{i}. Why did you like Python Programming Language only: ")
    with open("like.txt",'a')as file:
        file.write(f"\n{user}")
    i += 1
    