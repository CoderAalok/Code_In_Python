

"""
Iterable : { __iter__() or getitems() } The object is iterable like string, list, tuple, set
Iterator :  Traverse the iterable object using __iter__() and next()--> sometime along with yield also
Iteration: Iteration of iterable object one by one (Overall, iteration is process which iterate the object)
"""
# Generator function: Generator function creates genereator object that hold execution state, and using next() method to produced one by one elements
# Fibonaccii Generator 
# n = 5
# def fibo(n):
#     n1, n2 = 0, 1
#     while n1 <= n:
#         yield n1 # object generate
#         n1,n2 = n2, n1+n2

# f = fibo(n) #generator object
# for _ in range(n):
#     print(next(f))
    
    # OR
    
# for x in f:
#     print((x), end=" ")

def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact *= x
        yield fact

n = 5
fact = factorial(n)  # generator object (holds execution state)
for _ in range(6):
    print(next(fact))


# Throws an error due to no more next iteration yet means stop iteration
    print(next(fact))
