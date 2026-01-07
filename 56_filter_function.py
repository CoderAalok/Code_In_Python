
# Nested Logic
def check_even_odd():
    def is_even(n):
        return n%2 == 0
    return is_even

li_num = [1,2,3,5,6,8]
call_inn = check_even_odd()
even = list(filter(call_inn,li_num))
print(even)


# def check_even_odd(numbers):
#     def is_even(n):
#         return n%2 == 0
#     return list(filter(is_even,numbers))

# li_num = [1,2,3,5,6,8]
# call_inn = check_even_odd(li_num)
# print(call_inn)


# def fun(x):
#     return x%2 != 0
# li = [2,3,15,6]
# re = min(filter(fun,li))
# print(re) 

li1 = [1,2,3,4]
li2 = [3,5,1,7]
res = list(filter(lambda x: x**2>x*2,li2)) #select those elements which satisfy the condition
print(res)
