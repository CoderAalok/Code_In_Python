# def permutation(word):
#     if not word:
#         return None
#     li = []  #packed list are stored
#     li1 = []
#     arr = ''
#     lenn = len(word)
#     for i in word:
#         seen = [i]
#         for j in word:
#             if j not in seen:
#                 seen.append(j)
#         li.append(seen)
#     for k in li: #reduce packed list
        
#         for q in k:
#             arr += q
#         li1.append(arr)
#         arr = ''
        
#     return li1
# print(permutation('1234'))


def permutation(word):
    if len(word) == 0:
        return []
    if len(word) == 1:
        return [word]

    re = []
    for i in range(len(word)):
        fir = word[i]
        sec = word[:i] + word[i+1:]
        for ch in permutation(sec):   #Recursively executes
            re.append(fir+ch)
    return re

print(permutation('Alok'))
