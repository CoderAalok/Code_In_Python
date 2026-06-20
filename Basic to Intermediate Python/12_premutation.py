# def rotation(word):
#     if not word:
#         return None
#     li = []  #packed list are stored
#     for i in range(len(word)):
#         rot_word = word[i:] + word[:i]
#         li.append(rot_word)
        
#     return li
# print(rotation('1234'))


# def permutations(word):
#     if len(word) == 0:
#         return []
#     if len(word) == 1:
#         return [word]

#     re = []
#     for i in range(len(word)):
#         fir = word[i]
#         sec = word[:i] + word[i+1:]
#         for ch in permutations(sec):   #Recursively executes
#             re.append(fir+ch)
#     return re

# print(permutations('cat'))


from itertools import permutations
for word in permutations("cat"):
    print(word)