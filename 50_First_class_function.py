

# # Closure in inner function(Remember that value from outer function)
# def fun1(x):
#     def fun2():
#         print(x*2*x)  
#     fun2()
# fun1(5)


# # Encapsulate of helper functions

# def search(texts):
#     def remove_whitespace():
#         print(''.join([t for t in texts.split()]))
#     remove_whitespace()

#     # def remove_special_character():
#     #     return texts.replace(" ! ","")
#     # return remove_special_character()
    
#     # def whitespace():
#     #     return [text.strip() for text in texts]  #closure function implementation
#     # return whitespace()

# # print(f"Did you mean: {search("co ! de cam ! p")}")

# print(f"Before Remove whitespaces: {(["  Debugging   ","   Dynamically"])}")
# print(f"After Remove whitespaces: {search(["  Debugging   ","   Dynamically"])}")

# search #Just read the code

# Question: 1

# def greet(name):
#     def message():
#         print(f"Hello, <{name}>!")

#     return message

# res = greet("World")
# res() #call -> message -> function

# Question: 2
# def power(n):
#     def square(x):
#         return x**n
#     return square

# res = power(5) #return -> square
# print(res(2))

# Accessing Outer Variables
# def counter(start):

#     def increment():
#         nonlocal start
#         start += 1
#         return start 
#     return increment

# increment = counter(5)

# print(increment())
# print(increment())
# print(increment())
