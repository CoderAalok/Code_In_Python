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

