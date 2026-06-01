# for i in range(2 , 21):
#     with open(f"table.txt {i}", "w")as t:
#          for j in range(1, 11):
#             res = i * j
#             if j != 10:
#                 t.write(f"{i} x {j} = {res}\n")  
#             else:
#                 t.write(f"{i} x {j} ={res}")


# with open("table.txt", "r")as fault:
#     pick = fault.read()
# pick = pick.replace("lol useless" , "$$$#####")
# with open("table.txt", "w")as fault:
#     fault.write(pick)


# def game(s):
#     return s
# new_score = game(100000)
# with open('score.txt','r')as f:
#     old_score = f.readline()
# with open('score.txt','w')as f:
#     if old_score == 0 :
#         f.write(f'The new Hi-score is {new_score}')
#     elif old_score < str(new_score):
#         f.write(f'The new Hi-score is {new_score}')
        
#Repeat such a censored word
# li = ['hey','come on', 'lets play','call me']
# for i in range(1,len(li)+1):
#     with open(f"pop.txt", "+a")as q:
#         for j in li:
#             q.write(f'{j} \n')
    

# file = open("log.txt",'w')
# file.write("Python is most popular programming language.")
# file.close()
# with open("log.txt", 'r')as file:
#     re = file.read()
# if "Python" in re:
#     print("Yes! the word 'Python' present in log file.")
# else:
#     print("No! the word 'Python not present in log file.")

# i = 1
# with open("Detect.txt", 'r')as f:
#     while True:
#         caught = f.readline()
#         if caught == '':  # this handling empty string...
#             break   
#         elif 'python' in caught.lower():
#             print(f"The word 'Python' present on {i} line. ")
#         else:
#             print(f"The word 'Python' not present on {i} line.")  
        
#         i += 1

import shutil  #this module is used to copy the content to the another file.
file = "GitHub_Setup.txt" #old file

file1 = "words.txt" #new file 
shutil.copyfile(file, file1)

#Opening file 
# ✅ r+ → Correct

# ❌ +r → Invalid

# ✅ w+ → Correct

# ❌ +w → Invalid

# f = open("rag.txt", 'w')
# q = f.write("Technology rapidly grow up and become more advanced.")
# print(q)
# f.close
# f = open("rag.txt", "r")
# q = f.read() #when input some argument on it then it print number of character.
# print(q)
# f.close


# f = open("rag.txt", 'a')
# f.write("Programmer can only create app or web-site by using AI.")
# f.close

# f = open('rag.txt', 'a+')
# f.write('Large Language Model')
# a= f.read(15)
# print(a)
# f.close()

# with open("rag.txt","a+")as size:
#     #size.read()
#     size.write("retrieval augmented generation")
    
# file = open('data.txt', 'r')
# #q = file.write('The human could not recogonize them self.')
# q = file.readline()
# print(q)
# file.close()

#Creating  a new file...
# f = open('pop.txt','w')
# q = f.write('Twinkel Twinkel litel star.')
# print(q)
# f.close()
# with open('pop.txt','r')as f:   
#     a = f.read()
#     if "Twinkel " in a:
#         print("yes")
#     else:
#         print("no")
# f.close()


# with open('file.c' , 'w')as f:
#     f.write('Application Layer')

# file = b'101011'
# with open('binary.bin', 'wb')as f:
#     f.write(file) # this gives an integer so we cannot decode it.
#     decode = file.decode('UTF-8') #binary(byte) code get decode. 
#     #for decode must be bytes needed
#     print(type(decode)) #class 'str'
#     #encode() convert string to byte
#     encode = decode.encode('utf-8')  #for encode must be string needed
#     print(type(encode)) #class bytes


# words = input("Enter a word: ")
# with open('count.txt','r')as cenc:
#     re = cenc.readlines()
# if words in re:
#     print("????")
# else:
#     print('</>')

# words = ['session','illegel site' 'unique','trobleshoot','harmful']
# with open('count.txt','r')as f:
#     re = f.read()
# for w in words:
#     re =re.replace(w,'123')
#     with open('count.txt','w')as k:
#        z = k.write(re)
#        print(z)
    # if w in re:
    #     print("?????")
    # else:
    #     print(0)

word = 'AI'
with open('detect.txt','r')as f:
    re = f.readlines()
for i , val in enumerate(re):
    if word in val :
        print(f"The word {word} on {i+1} line")
