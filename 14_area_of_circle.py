#PRIME NUMBER
# num = int(input("Enter the number :"))
# i = 1
# print("The prime number is ")
# while i<= num:
#     if num %i == 0:
#         print(i,end='')
#         i += 1
#     break

# To list out the all prime numbers of given number.
# num = int(input("Enter the number :"))
# prime = []
# for i in range(2, num+1):
#     count = 0
#     for j in range(1,i+1):
#         if i %j == 0:
#             count += 1
#     if count == 2:
#         prime.append(i)
# print(f"The {num} of Prime Numbers are {prime}.")


# Using funciton to find whether the given number is prime or not.

from sympy import *
n1 , n2 ,n3  = 5 , 3 ,10
print(isprime(20))
print(isprime(n1),isprime(n2),isprime(n3))
