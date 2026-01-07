x = 40 
def fun_global():
    print(x)  #read global variable only
fun_global()


x = 40 
def fun_global():
    global x
    # x *= 5
    print(x)  #read global variable  and modify by 'global' keyword 
fun_global()
print(x) 







# Assign function as variable

# def fun(x):
#     def grok(y):
#         return x+y
#     return grok

# var = fun(10)
# print(var(10))


# # Passing function as argument

# def gpai(strr):
#     return f"Hi! {strr}"

# def gpt(fun1,strr1):
#     return fun1(strr1)

# fun2 = gpt
# print(fun2(gpai,"gpai"))


# def outer(rag):
#     def inner():
#         return f"{rag.title()} based AI."
#     return inner()
    
# print(outer("rag"))

# li = [1,2,3,4,5]

# def first(li):
#     return f"Original: {li}"

# org = first
# print(org(li))

# def second(rem):
#     print(f"Before remove: {rem}")
#     rem.remove(2)
#     print(f"{rem}")
# second(li)

# def third(add):
#     add.insert(1,2)
#     print(f"Re-create original list: {add}")

# third(li)

# def add(num):
#     return  sum([n for n in num])

# def sub(num):
#     _sub = 0
#     for n in num:
#         _sub -= n 
#     return _sub

# def mul(num):
#     multi = 1
#     for n in num:
#         multi = n * multi
#     return multi

# cal = {
#     'add':add,
#     'sub':sub,
#     'mul':mul
# }
# number = list(map(int,input("Enter Numbers: ").split()))
# print(f"{list(cal.keys())}")
# user = input('Enter it:  ')
# key = cal[user]
# print(key(number))



# Find value of x and y from given equations
# 2x1 + 3y1 = 5
# 2x2 + 6y2 = 1

# class Equation:
#     def __init__(self,x1,y1,c1,x2,y2,c2):
#         self.x1 = x1
#         self.y1 = y1 
#         self.c1 = c1
        
#         self.x2 = x2
#         self.y2 = y2 
#         self.c2 = c2
        
# class Solution(Equation):
#     def solve(self):
        
#         if abs(self.x1) == abs(self.x2):
#             x = abs(self.x1) - abs(self.x2)
#             y = (self.y1) + (-self.y2)
#             c = (self.c1) + (-self.c2)
            
#             y = round(self.c/self.y)
            
#             x = round((self.c1-(self.y*self.y1))/self.x1)
            
#             return (x,y)

# x1,y1,c1 = 2,3,6
# x2,y2,c2 = 2,6,0

# eq = Solution(x1,y1,c1,x2,y2,c2)
# print(f"(x, y) = {eq.solve()}")