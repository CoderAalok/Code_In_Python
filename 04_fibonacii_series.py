<<<<<<< HEAD
# find the Fibonacci series of n number.
# It makes two sense, either the length of series equal to given number or last a digit less or equal to number


#Method-1( "Range_fibonacii_series" != given number)

# num = 10#int(input("enter a number :"))
# n1 , n2 = 0 , 1
# fibo = []

# while n1 < num:
    
#     fibo.append(n1)
#     n1 , n2 = n2 , n1+n2
    
# print(f'The fibonacii series of given nummber {num} is :',end=' ')
# for i in fibo:
#     print(i,end=' ')


# Method-2 ( "Count_fibonacii_series" == given number)

# num = int(input('Enter a number : '))
# n1 , n2 = 0 ,1
# fibo = [n1]
# for i in range(1 , num+1):
#     n1 , n2 = n2 , n1+n2
#     fibo.append(n1)
# print(f'The fibonacii sxeries of given nummber {num} is : {fibo}')


#Approach of fibonacci's series

# def fib(N):
#     n1 , n2 = 0,1
#     fibo = []
#     while n1 <= N:
#         fibo.append(n1)
#         n1 ,n2 = n2 , n1+n2
#     return fibo
# print(fib(5))

# To finding the given number is fibonacci's series or not


# def fib(N):
#     if N < 0:
#         return None
#     n1 , n2 = 0,1
#     fibo = []
#     while n1 <= N:
#         fibo.append(n1)
#         n1 ,n2 = n2 , n1+n2
#     if N in fibo :
#         return True
#     return False
# N = int(input("Enter a number : "))
# print(f"The  given number {N} is Fibonacci's series {fib(N)}")

# Method-2

# def fib(N):
#     if N < 0:
#         return None
#     n1 , n2 = 0,1
#     while n1 <= N:
#        if n1 == N:
#            return True
#        n1 , n2 = n2 , n1 + n2
#     return False
       
# N = int(input("Enter a number : "))
# #print(f"The  given number {N} is Fibonacci's series, here>>> {fib(N)} : ")
# if fib(N):
#     print(f"The given number {N} is a Fibonacci's Series.")
# else:
#     print(f"The given number {N} is not a Fibonacci's Series.")

'''Nth multiple of a number in Fibonacci Series'''
=======
# find the Fibonacci series of n number.
# It makes two sense, either the length of series equal to given number or last a digit less or equal to number


#Method-1( "Range_fibonacii_series" != given number)

# num = 10#int(input("enter a number :"))
# n1 , n2 = 0 , 1
# fibo = []

# while n1 < num:
    
#     fibo.append(n1)
#     n1 , n2 = n2 , n1+n2
    
# print(f'The fibonacii series of given nummber {num} is :',end=' ')
# for i in fibo:
#     print(i,end=' ')


# Method-2 ( "Count_fibonacii_series" == given number)

# num = int(input('Enter a number : '))
# n1 , n2 = 0 ,1
# fibo = [n1]
# for i in range(1 , num+1):
#     n1 , n2 = n2 , n1+n2
#     fibo.append(n1)
# print(f'The fibonacii sxeries of given nummber {num} is : {fibo}')


#Approach of fibonacci's series

# def fib(N):
#     n1 , n2 = 0,1
#     fibo = []
#     while n1 <= N:
#         fibo.append(n1)
#         n1 ,n2 = n2 , n1+n2
#     return fibo
# print(fib(5))

# To finding the given number is fibonacci's series or not


# def fib(N):
#     if N < 0:
#         return None
#     n1 , n2 = 0,1
#     fibo = []
#     while n1 <= N:
#         fibo.append(n1)
#         n1 ,n2 = n2 , n1+n2
#     if N in fibo :
#         return True
#     return False
# N = int(input("Enter a number : "))
# print(f"The  given number {N} is Fibonacci's series {fib(N)}")

# Method-2

# def fib(N):
#     if N < 0:
#         return None
#     n1 , n2 = 0,1
#     while n1 <= N:
#        if n1 == N:
#            return True
#        n1 , n2 = n2 , n1 + n2
#     return False
       
# N = int(input("Enter a number : "))
# #print(f"The  given number {N} is Fibonacci's series, here>>> {fib(N)} : ")
# if fib(N):
#     print(f"The given number {N} is a Fibonacci's Series.")
# else:
#     print(f"The given number {N} is not a Fibonacci's Series.")

'''Nth multiple of a number in Fibonacci Series'''
>>>>>>> aa2e7dcd15f91be88c03e886b9e67eae8692673b
