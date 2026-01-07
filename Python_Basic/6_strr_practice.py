# Find words which are greater than given length k

# def greater_words(strr,k):

#     if not isinstance(strr,str) or k < 0:
#         return None
    
#     words = strr.split()
#     for word in (words):
#             if len(word) > k:
#                 print(word)
            
# strr = ('Protocal is rulebook for communication between devices on internet')
# k = -6
# greater_words(strr,k)

from collections import Counter
def remove_char(strr):
    if not isinstance(strr,str):
        return None   #Immeditly Pause
    char_count = Counter(strr)
    count = max(char_count, key = char_count.get)
    print(strr.replace(count,''))
    print(count)
#     dic_char = {}
#     for i in strr:  #key
#         le = strr.count(i)  #value
#         if i != ' ' and i not in dic_char :
#             dic_char[i] = le
#     len_val = max(dic_char.values())
#     rev = [ch for ch , val in dic_char.items()  if val == len_val ]
#     for i in rev:
#        return strr.replace(i,'')
remove_char(('Python is too good language for beginner'))        
# print(remove_char(('Python is too good language for beginner')))    

#removing i'th character
s = 'PythonProgramming'
li = list(s)
rev = ''.join([ch for ch in li if ch != 'o'])
print(rev)
i= 4
rev = s[:i] + s[i+1:]
print(rev)