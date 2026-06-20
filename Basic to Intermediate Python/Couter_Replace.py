# def counter(strr):
#     if not strr:
#         return None

#     count = {}
#     for ch in strr:
#         value = strr.count(ch)
#         if ch not in count and ch != ' ' and value >1:
#             count[ch] = valuejgdsiaa
#     return list(count)
# print(counter('BootCamp of Python learning'))



# Replace all occurrences(possible outcomes of word) of a substring(word) in a string

# strr = ("Computer Algorithm one of most important to visullize all senario's of computer").lower()
# sub_string = strr.split()
# print(strr.replace('computer','Quantum Computer'))
# tar = 'computer of most'.split()
# rep = 'Quantum Computer'
# i = 0

# while tar[i] in sub_string and i != len(tar)-1:
#     print(strr.replace(tar[i],'###'))
#     i += 1



# Duplicate Words replace
# strr = ("Computer Algorithm one of most important to visullize all senario's of computer").lower()
# seen = set()
# sub_string = strr.split()

# for indx,word in enumerate(sub_string):
#     if word in seen:
#         sub_string[indx] = '.....'
#     else:
#         seen.add(word)
# print(' '.join(sub_string))

# Remove white spaces and dots from string
# def remove_whitespace_and_dots(text):
#     # Remove whitespace
#     text = text.replace(" ", "")
#     # Remove dots
#     text = text.replace(".", "")
#     return text

# # Example usage
# test_string = "Hello... World   with.  spaces. and. dots..."
# cleaned_string = remove_whitespace_and_dots(test_string)
# print("Original string:", test_string)
# print("Cleaned string:", cleaned_string)  # Output: HelloWorldwithspacesanddots

