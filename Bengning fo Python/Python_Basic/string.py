#str="123456789"
#print(",".join(str))
#s=1,2,3,4,5,6,7,8,9
#print(sum(s))


#a=1,3,4,5,4
#print(str(a))

#print(a.index(1))

#str=("1,3 2,6")
#print(str.rindex("6"))

#print(str.encode())

#b="str","Constant","uncountable"
#print(isinstance(a,(float,int,str)))
#print(isinstance(b,(float,int,str)))

#b.isalpha
#print(b.find("t"))      
#k="The RAG is stand for Retrieval Argumented Generation."

#print(k.count("e"))
#print(k.swapcase())#small alphabet undergoes to capital and vice versa...

#q="8,5,6,4,2,7"
#print(q.rjust(100))#just move right side

#print(k.center(55))

# Ways to remove i’th character from string

# string = 'Compitative Programming'
# strr = list(string)
# strr.pop(3)
# # print(''.join(strr))
# for i in strr:
#     print(i, end='')

# for k in range(len(strr)):
#     if k ==3:
#         strr.remove(strr[k])
#         break
# for i in strr:
#     print(i, end='')

# string = 'Compitative Programming'
# strr = string.replace('a', '')
# print(strr)



# Check if a Substring is Present in a Given String
#method-1
# strr = 'silent is power of intelligence'
# substring = 'silent'
# if substring in strr:
#     print("Yes the substring is present in string.")
# else:
#     print("No any substring present in string.")
    
# strr = ('silent is power of intelligence').split()
# substring = 'silent'
# result = [True if substring in strr else False]
# print(result)
# if substring in strr:
#     print(True)
# else: 
#     print(False)

# # Words Frequency in String Shorthands
# strr = ("This is a sample sentence. This sentence is just a sample.").split()

# # 'as we know that lots of platform totally fake and they try to scam our information'
# freq_words = {}
# for i in strr:
#     if not i in freq_words:
#         freq_words[i] = 1
#     else:
#         freq_words[i] += 1
# # for k in freq_words.items():
# #     print(f" {k} ") 
# for _ , val in enumerate(freq_words):
#     print(f"{val}:-> {freq_words[val]}")

# Convert Snake case to Pascal case
# strr = ('python is one of the most popular programming language')
# re = ''.join(strr.title().strip() )
# print(re.replace(" ",''))  #PascalCase

# mat = [ [2,3] ,
#        [4,6]    
# ]
# col = [[mat[r][c] for r in range(len(mat))] for c in range(len(mat[0]))]
# print(col)

#method-1
# strr = "Convert Snake case to Pascal case"
# print(len(strr))

# #method-2
# count = 0
# for i in strr:
#     count += 1
# print(count)

# Accept the strings which contains all vowels
# strr = ('Retrievalou Argumented  Generationu Quantum aeComputing').split().lower()
# vol = 'aeiou'
# re = [i for i in strr if all(v in i for v in vol)]  
# print(re) 
# # re = [(val) for _ , val in enumerate(strr) if len(val) %2 == 0]
# # print(re)

# vowel = ['a','e','i','o','u']
# count = 0
# vowel_word = []
# for i in strr:
#     for j in vowel:
#         if j in set(i):
#             count += 1
#     if count == len(vowel):
#         vowel_word.append(i)
#     count = 0
# print(vowel_word)

# strr = ('Retrieval Argumented  Generation Quantum Computing')
# # re = strr.replace('e','')
# # print(re)

# re = strr.find("G")   #index of first character countable
# rev  = strr[:re] + strr[re+1:]
# print(rev)




# Count the Number of matching characters in a pair of string
#In this, we are counting all unique characters matching in both strings 
# strr1 = 'Retrieval'.lower()
# strr2 = 'Python Intrerpreter'.lower()
# count = 0
# rel = [i for i in strr1 if i in strr2]
# print(f'{rel} ->>{len(rel)}')

# #this count all repeating characters matching in both strings
# for i in strr1:
#     for j in strr2:
#         if i == j:
#             count += 1
# print(f'So there are {count} characters are matching in a pair of strings.')

# rep = 'Extreemllyy'.lower()
# # To find the duplicate no. of characters
# dic = {}
# for i in rep:
#     s = rep.count(i)
#     if not i in dic:
#         dic[i] = s
# print(f"Here the unique string with characters -> {''.join(dic.keys())}")
# # result_unique= [k for k ,_ in dic.items()]
# # result_nonunique = [k for k ,v in dic.items() if v>1 ]
# # print(f"Here the non-unique string with character -> {rep}")
# print(f"Here the unique string with characters -> {''.join(dic.keys())}")
# print(f"Here the no. of non-unique characters -> {''.join(result_nonunique)}")

# count = {}
# for i in rep :
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1


# rel = [k for k ,_ in count.items()  ]
# print(''.join(rel))

# rep = 'Extreemllyy'
# result = ''.join(dict.fromkeys(rep))
# print(f"{''.join(result)}") 

# strr = 'silicovolcanoconiousios'
# unique = set()
# rev = ''
# for i in strr:
#     if i not in unique:
#         unique.add(i)
#         rev += i
# print(f"Here unique string with characters : {rev}")

#Least frequency character in a string(minimum appears character)
# strr = "The most expensive in this world is our skill with knowledge".lower()
# least = {}  #stored each character with it's appearing time
# for ch in strr:
#     if ch == ' ':  #skip spaces
#         continue
#     val_ch = strr.count(ch)   
#     if ch not in least :   
#         least[ch] = val_ch
# size = min(least.values())  #least frequency length of character
# result = [k for k ,v in least.items() if v == size ]
# print(f"Here the least frequency characters -> {result}")




# strr = "The most expensive in this world is our skill with knowledge".split()
# len_freq = [len(i) for i in strr ]
# least = min(len_freq)

# least_freq = [l for l in strr if len(l) == least]

# print(f"The shorest words -> {' '.join(least_freq)}")



# s1 = 'encapsulation'
# s2 = 'abstraction'
# count = 0
# ch = []
# for i in s1:
#     if i in  s2 and i not in ch:
#         count += 1
#         ch.append(i)
# print(f"Here the pair no. of strings -> {count} and {ch}")

format_strr = "AI is {0} changing the world. ".format("powerful which")
print(format_strr)