#https://developer.mozilla.org


# Method-I (To check URL in a text)
# def url_detect(text):
#     if not text:
#         return None
#     if 'https://' in text or 'www.' in text:
#         print("URL is found.")   #URL: Uniform Resources Locator
#     else:
#         print('No URL is found.')
# url_detect('https://developer.mozilla.org')

# import re
# def url_dectetor(text):

#     if not text:
#         return None

#     patt = r"(https?://[^\s]+|www\.[^\s]+)"
#     if re.findall(patt,text):
#         print("URL is found." + text)   #URL: Uniform Resources Locator
#     else:
#         print("No URL is found.")

# url_dectetor('https://developer.mozilla.org')


# Dynamic Code Execution: Python can execute code dynamically using functions like 
# eval() and exec(), which allow strings of code to be run during runtime.
# code = 'a=34\nb=23\nprint(a+b)'


# code = '111111+221'
# try:
#     print(eval(code))
# except SyntaxError:
#     print("Invalid input!")
# code_ = '''x=114
# y=12
# z = x+y
# print(x+y)'''

# (exec(code_))
# print(z)


