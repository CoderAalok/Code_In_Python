
# # Method-I
# files = ["file1.txt","file2.txt","file3.txt"]
# for f in files:
#     try:
#         with open(f)as f:
#             file = f.read()
#         if file:
#             print("The file is exit.")
#             continue
                
#     except FileNotFoundError:
#         print("The file not found")
#         continue

# # Method-II
# def check_file(file):
#     try:
#         with open(file)as f:
#             print(f.read())

#     except FileNotFoundError as e:
#         print(e)

# for f in files:
#     check_file(f)

# # ========================================================


# # li = [1,2,3,4,4,5,7,8,9,12]
# # for i,v in enumerate(li):
# #     if i in [2,4,6]:
# #         print(f"Position: {i+1} and Value: {v}")

# # n = int(input("Enter a number: ").strip())
# # table = [n*i for i in range(1,11)]
# # print(table)
# # ========================================================
# a = int(input().strip())
# b = int(input().strip())
# try:
#     div = a/b
#     print(f"Division of {a} and {b} = {div}")
# except ZeroDivisionError:
#     print("Undefined!")



# # try:
# #     name = input("Enter yout Name: ").strip()
# #     marks = int(input("Enter your Marks: ").strip())
# #     phn_num = int(input("Enter your Phone Number: ").strip())
    
# #     std_data = "The name of the student is {0}, his marks are {1} and phone number is {2}".format(name,phn_num,marks)
# #     print(std_data)
# # except ValueError as e:
# #     print(e)
# # ========================================================
  
# n = 17
# table = [n*i for i in range(1,11)]
# for i,num in enumerate(table, start=1):
#     print(f"{n}*{i} = {num:<20}")

# li = [1,5,20,15,35,2,32,32,23,100]
# div = list(filter(lambda x: x%5 == 0, li))
# print(div)
# # ========================================================

# from functools import reduce
# li = [1,5,20,15,35,2,32,32,23,100]
# def fun(x,y):
#     return x if x>y else y

# maximum = reduce(fun,li)
# maximum = reduce(max,li)
# print(maximum)

