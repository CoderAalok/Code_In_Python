# Check if a string contains any special character

def special_detector(text,special):
    if text.isdigit() or text == "":
        print(" Input type is missing! ")
        return
    
    count_special_char  = []
    count_len = 0
    
    for ch in special:
        count_len += text.count(ch)
        if ch in text:
            count_special_char.append(ch)
            
    if count_special_char:
       print(f"-> {count_len} Special character's ({','.join(count_special_char)}) in given text!  ") 
    else:
        print("Fine! No one special character detect.")
    
text = "1python2@"
special = "@!~#$%^&-*_[]<>.,/|{}`=+"
special_detector(text,special)


# def special_character(strr):
#     if  strr.isdigit() or strr == ' ':
#         return False
#     return True
# strr = "Pythonic!"
# special_char = "@!~#$%^&-*_[]<>.,/|{}`=+"
# result = special_character(strr)
# if result:
#     detect = [catch for catch in special_char if catch in strr if catch != '']
#     len_special_char = len(detect)
    
#     print(f"'{len_special_char}' Special character's used in text. ")
    
# else:
#     print(" Input type is Missing! ")
    
    

# #In this method only concatenated string from detect also if get space also it count  
# def detect(strr):
#     if not strr.isalpha() :
#         return True
#     return False
# strr = "Python!@"
# result = detect(strr)
# if result:
#     print(f"⚠️  Warning special character's used in text. ")
# else:
#     print(" fine! ")



#Alternative
# strr = "#RAG based AI@"
# special = '@!~#$%^&*_[]<>/|'
# detect = [ch for ch in special if ch in strr if ch != '']
# count = len(detect)
# # for i in special:
# #     if i in detect:
# #         count += 1
# print(f"{count}: Special character is found in your tex ->{detect}. ")


# s = 'python@'
# if s.isalpha():
#     print(s.isalpha())
# else:
#     print("False!")