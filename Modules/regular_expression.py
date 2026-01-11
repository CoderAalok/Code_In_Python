
import re
# print(dir(re))
strr = "The Gen-AI all most reached at human's level," \
" Gen-AI do all possible works that human's can do may be more."

# strr_num = "909york"

# format = re.compile(r'\d{1}')
# print(format.match(strr_num), "->",strr_num[0:1])


# matches = re.compile(r'.AI')  #gives iterable object
# for match in matches.finditer(strr):
#     print(match.group())

# matches = re.compile(r'^The')

# matches = re.compile(r'mo$')
# for match in matches.finditer(strr):
#     print(match.group())

# match = re.search('A', strr)
# pattern = re.compile(r'AI*')

# print(pattern.search(strr))

# a = "python@gmail.com"
# pattern1 = re.compile(r'(@gmail.com)')

# pattern = re.compile(r'.+@gmail\.com') #-> fullmatch(a)
# print(bool(pattern.fullmatch(a)))

# pattern1 = re.compile(r'@gmail.com$')

# if pattern1.search(a):
#     print(True)
# else:
#     print(False)

# pattern = re.compile(r'.Gen-AI*')
# print((pattern.search(strr)))

# ph = "Here some employes contact number " \
# "+977-9890988090" \
# "+977-9823419999" \
# "+977-9842145211" \
# "+977-9834214520"
# phones_number = []
# patt = re.compile(r'\+977-\d{10}')
# for phone in patt.finditer(ph):
#     phones_number.append(phone.group())
# print(phones_number)

# emails = """ 
# While coordinating vendor audits,
#  the team exchanged notes with Google’s
#    escalation desk Support.Team@google.com late at night;
#      meanwhile an internal memo referenced microsoft-help@microsoft.com though
#        not all tickets were valid. Orders flagged as urgent were forwarded to
#          “customer.service+priority@amazon.com”, and a legacy document oddly
#            listed INFO@meta.com next to deprecated URLs. During a streaming outage,
#              someone mistakenly typed support@netflix.com
#                before correcting it to support@netflix.com, 
#                and finally a research proposal draft mentioned 
#                contact research@openai.com in the footer.

# """

# email_collector = []

# pattern = re.compile(r'[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9_.%+-]+\.com')   #matching pattern of email

# print(pattern.findall(emails))
# for email in pattern.finditer(emails): 
#     email_collector.append(email.group())
# print(email_collector)


# pattern = re.compile(r'[A-z]')
# print(pattern.search(strr))  
# for p in pattern.finditer(strr):
#     print(p)


# pattern = re.compile(r'AI')
# print(pattern.findall(strr))

# strr = "cowcowcow"
# pattern = re.compile(r'[cow]*')
# print(pattern.match(strr))
