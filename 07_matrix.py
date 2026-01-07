# # key = "windows"
# # key_1 = {"window":"11-pro", "apple":"fruits"}
# # # if key in key_1:
# #     print(key_1[key])#this  is simple method and large time complexicity

# # else:
# #     print(None)

# # val = key_1.get(key)# this good for use

# # print(val)

# # print(hash('[cartoon]'))


# #LIST COMPREHENSIONS:filtering the elements and then passing in the coscise expression
# # li = [1,2,3,4,5,6,34,2,454,3,23,5]
# # even = [i for i in li if i %2 ==0]
# # print(even)               

# # words = ["planet","Health_resource","magnified","Networling","satellite", "Geostationary","uniform"]
# # result = [i for i in words if len(i) > 7]
# # print(result)

# #SET COMPREHENSIONS
# sat = {1,3,43,9,0,7,-9,-8}
# val = {val for i, val in enumerate(sat) if val >0}
# print(val)

# #DICT COMPREHENSIONS
# data = ["garbage","Empty","Hyperbola","Ellipse"]
# dict_ = {i : val for i, val in enumerate(data) }
# print(dict_) 


# li = ["client","Artitecture","sofware", "database","file_handling","topology","Encaptulation","Inreritance","Polymorphsim"]

# result = [val for val in li if val.count('a') > 1]
# print(result)

# name = list(input("Enter your name : ").capitalize().split())
# last = list(input("Enter your last name : ").capitalize().split())
# for result in zip(name, last):
#     print(result)
# 