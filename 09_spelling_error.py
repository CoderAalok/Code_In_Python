# def table(num):
#     for i in range(1,11):
#         result = num * i
#         print(f"{num} * {i} = {result}")
# table(5)

# name = input("Enter your name : ")
# print("Good Morning,"+ name)

# letter = '''Dear,|NAME|\n Congratulation, you're haired in our company on DATE.\n And we're welcome in company. We wise you will definetly achive all those thing which do you want.\n
# Thank you!
# '''
# name = input("Enter a name : ")
# date = input("Enter the date  : ")
# result = letter.replace("NAME",name)
# last = result.replace("DATE",date)
# print(last)

# list_fruits = []
# fruits =  (input("Enter your favourite fruits name : "))
# list_fruits.append(fruits)
# while True:
#     try:      
#         add_f = input("Adding more your favourite fruits name [YES \ NO ]: ").strip().lower()
#         if add_f == 'yes':
#             fruits =  (input("So, enter it \n \t : "))
#             list_fruits.append(fruits)
#         elif add_f == 'no':
#             break
#         else:
#             print("Either [YES OR NO]")   
#     except Exception:
#         print("Only valid input type")
#         break
# print(list_fruits)


# li1 = input("Enter 1 ")
# li2 = input("Enter 2")
# li3 = input("Enter 3 ")
# li4 = input("Enter 4 ")
# li5 = input("Enter 5 ")
# li6 = input("Enter 6 ")
# li7 = input("Enter 7 ")
# items= {li1,li2,li3,li4,li5,li6,li7}
# print(items)


# tuple =(1,3,3,3,4,5,2,2)
# li =(2,3,4,3)
# print(tuple.count(3))

#pass _ fail percentge
# sub1 = int(input("Enter first Subject marks out of 75:" ))
# sub2 = int(input("Enter second Subject marks out of 75:" ))
# sub3 = int(input("Enter third Subject marks out of 75 :" ))
# total = ((sub1 + sub2 + sub3)*100)//300

# if sub1 and sub2 and sub3 <30:
#     print(f"You are fail ")
# else:
#     print(f"Congrutlation you are passed in all three subject with {total}%")

#spam comment detector
# import re 
# spam_comment = ["hack", "illegal","fishing","scam"]
# user = input("Search anything which do you want...").lower().strip()

# catch = [i for i in spam_comment if re.search(rf"\b{re.escape(i)}\b", user)]
# if catch:
#     print("Warnnig! leave immeditely this cause your device.")
# else:
#     print("Safe you are in right track...")

# spam_comment = ["hack", "illegal","fishing","scam"]
# user = input("Search anything which do you want...").lower().strip().split()
# found = [pick for pick in user if pick in spam_comment ]
# if found:
#     print("Warnnig! leave immeditely this cause your device.")
# else:
#     print("Safe you are in right track...")

#Username and Password detector 
# while True:
#     username = input("Enter you username : ")
#     password = input("Enter your password : ")
#     if len(username) < 5 and len(password) <8:
#         print("Username  and Password must be greater than 5 and 8.")
#     elif len(username) <5:
#         print("Username must be 5 character.")
#     elif len(password) <8:
#         print("Password must be 8 character.")
#     else:
#         print("Sucessfully login...")
#         break

#Character based stored in list
# li  = []
# user = input("Enter your friend name including you...\n : ").split()
# for pick in user:
#     if pick[0]=='a':
#         li.append(pick)
# print(li)
    
num = int(input("Enter a number :"))
count = 0 
for i in range(1,num+1):
    if num % i ==  0 :
        count += 1
if count == 2:
        print(f"{num} is Prime Number.")
else:
        print(f"{num} is not Prime Number.")
              