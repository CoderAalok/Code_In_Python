

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

# from sympy import *
# n1 , n2 ,n3  = 5 , 3 ,10
# print(isprime(20))
# print(isprime(n1),isprime(n2),isprime(n3))



"""work but slow for larger number"""
# def isprime(n: int) -> bool:
#     if n <= 1:
#         return False
    
#     factors = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             factors += 1

#     return factors == 2

# print(isprime(11))


"""much more efficient than entire approach"""
def isprime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, (int(n**0.5) + 1)):  # including 'sqrt(n)'
        if n % i == 0:
            return False
    
    return True

print(isprime(41))

"""Workflow

n = 41

start:
i = 2

Loop run: int(sqrt(41)) -> 6 

41 % 2 == 0 (False)
41 % 3 == 0 (False)
41 % 4 == 0 (False)
41 % 5 == 0 (False)
41 % 6 == 0 (False)

end

return True

"""
"""
Time Complexity: O(sqrt(n))
Space Complexity: O(1)

"""