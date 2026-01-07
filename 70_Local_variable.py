# x = 90
# def local():
#     print(x)#90
# local()  #global variable read inside the function only
# print(x) #90

# x = 90
# def local():
#     x = 50
#     print(x)  #50  same variable but different output->global can't be modify
# local() 
# print(x) #90


# # Access to outer variable 
# def outer(x):
#     x *= 10  #local variable
#     def inner(y):
#         return (x**y)  #local to inner
    
#     print(inner(2)) # Normally call 
#     i = inner  #create a reference/ access a function to a variable
#     print(i(3)) #
    
#     def inner_1(z):
#         print("last call",z)
#     inner_1(z=x)
# outer(2)

