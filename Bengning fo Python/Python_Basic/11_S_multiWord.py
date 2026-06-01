# def multiWord(sent):

#     if not sent:
#         return None

#     text_word = sent.split()
#     word_replace = ['Burgger','Pizza','Noodles']

#     #Method 1: Using loop and enumerate
#     # for i,v in enumerate(text_word):
#     #     if v in word_replace:
#             # text_word[i] = "Fruits" #replace bad food
#     # return ' '.join(text_word)

#     #Method 2: Using str.replace() function
#     # for word in word_replace:
#     #     sent = sent.replace(word,"Fruits")
#     # return sent

#     #Method 3: Using List Comprehension
#     rep = ' '.join(["Fruits" if word in word_replace else word for word in text_word])
#     return rep

# print(multiWord("I like Burgger only.")) #Bad Food content replaced with Fruits