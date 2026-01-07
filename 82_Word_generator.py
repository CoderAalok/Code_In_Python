# Generating random strings until a given string is generated


# import random
# import  string
# orginal_word = "py"
# alpha = (string.ascii_lowercase)
# # new = ""
# attempt = 0
# while True:
#     attempt += 1
#     gen = ''.join(random.choice(alpha) for _ in range(len(orginal_word)))
#     if gen == orginal_word:
#         print(f"{attempt} -> {gen}")
#         break
# while True:
#     attempt += 1
#     for _ in range(len(orginal_word)):
#         gen = ''.join(random.choice(string.ascii_lowercase))
#         new += gen
#     if new == orginal_word:
#         print(f'Finally Attempt: {attempt}, generated: {new}')
#         break       
#     new = ""
#     continue

# while True:
#     attempt += 1
#     new_word  = ''.join(random.choice(string.ascii_lowercase)  for i in range(len(orginal_word)))
#     if new_word == orginal_word:
#         print(f"Attempt:{attempt}\nGen_word: {new_word}")
#         break
    
# while True:
#     attempt += 1
#     gen = random.choice(string.ascii_letters)
#     if gen in list(orginal_word):
#         new += gen
#         if new == orginal_word:
#             print(attempt,new)
#             break 
#         attempt -= 1


# import random
# import string

# orginal_word = "Python"
# place_holder = [""]*len(orginal_word)
# attempt = 0

# while ''.join(place_holder) != orginal_word:
#     attempt += 1
#     for i in range(len(orginal_word)):
#         if orginal_word[i] != place_holder[i]:
#             place_holder[i] = random.choice(string.ascii_letters)
#     print(f"{attempt} -> {''.join(place_holder)}")
    
    # Time complexity : O(26*n)
    
#Approach
import random, string
# import string
def generatation(target):
    if  not target.isalpha():
        return
    place_holder = [',']*len(target)
    attempt = 0
    while  ''.join(place_holder) != target:
        attempt += 1
        for i in range(len(target)):
            if target[i] != place_holder[i]:
                place_holder[i] = random.choice(string.ascii_letters )
    return attempt , ''.join(place_holder)

target = 'python'
result = generatation(target)
for i in result:
    if isinstance(i,int):
        print(f"Attempt: {i}")
    else:
        print(f"Generated_word: {i}")


# print(f"Attempt: {attempt}\n Generated_Word: {''.join(place_holder)}")