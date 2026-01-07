# count_line = 0
# count_word = ""
# with open('detect.txt', 'r')as f :
#     q = f.readlines()
#     for i , val in enumerate(q) :
#         count_line = i+1
#         count_word += val
# print(count_line)
# count_list = count_word.split()
# len_words = len(count_list)
# print(len_words)
# print(len(count_word))


#word detector   
count = []
with open("detect.txt",'r')as f:
    reads = f.readlines()
    for i,val in enumerate(reads):
        if "python" in val.lower():
           count.append(i+1)
if count:
    print(f"Yes! The word 'python' present on {count} line.")
else:
    print(f"No! The word 'python' not present on this file.")
            
    
#read the first n lines of a file (take n as input from the user).
user = int(input("How much lines do you want to reads :  "))
i = 1
with open("data.txt",'r')as f:
    while i <= user:
        re = f.readline() #this reads extra line after end of code
        if not re:
            break  #break at extra empty line
        print(re)
        i += 1

#Exceptional handiling (like FileNotFoundError)
# try:
#     with open("byte.txt",'r')as f:
#         f.read()
# except FileNotFoundError:
#     print("The file doesn't exits on your folder.")
       