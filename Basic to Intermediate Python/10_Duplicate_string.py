# def duplicate(string):
#     word_dup = string.split()
#     def_string = {"This":"It"}
#     new_string = []
#     for i, val in enumerate(word_dup):
#         if val in new_string:
#             if val in def_string:
#                 word_dup[i] = def_string[val]
#         new_string.append(val)
#     return ' '.join(word_dup)
# print(duplicate("This is good. This is not bad."))


# a = "This is good. This is, not` bad".split()
# for i in a:
#     c = (i.strip("'`!#@$.,'")).split()
#     for i in c:
#         print(i,end=' ')

# Replace duplicate occurance string: -> Replace occurrence of only duplicate, [i.e from second occurrence.]

# def duplicate(strr):
#     if not isinstance(strr,str):
#         return None
#     word = strr.split()
#     seen_word =  set()
#     defined_chr = {"This":"It's", "good":"gorgeous"}
#     for i , v in enumerate(word):
#         clear_special = v.strip("',.!`#~")
#         if clear_special in defined_chr:
#             if clear_special in seen_word:
#                 word[i] = defined_chr[v]
#             seen_word.add(v)
#     return ' '.join(word)

# print(duplicate("This is too good . This is good"))

def multiple_word(strr):
    word = strr.split()
    seen = set()
    # seen_word = [word[i] for i , v in word if v in seen ]
    
    # for idx , val in enumerate(word):
    #     # To remove special or whitespace if attach with word
    #     special = val.strip("~`.,!@#")
    #     if special in seen:
    #         # Replace the word by "K"
    #         word[idx] = '___' 
    #     seen.add(val)
    return ' '.join(word)
print(multiple_word("The most peacefull way God, Every time with or without anyone to be relax. The"))