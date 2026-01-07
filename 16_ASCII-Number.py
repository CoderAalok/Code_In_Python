#fibonacci's series

# def fibo(n):
#      if n <= 0:
#          return 0
#      elif n <= 1:
#           return 1
#      else:
#           return fibo(n-1) + fibo(n-2)
# for n in range(10):
#      print(fibo(n),end=' ')
     
#first natural number
# def natural(n):
#     if n<0 :
#         print("Exclude negative integer.")
#     elif n == 0:
#        return 0
#     else:
#        return n + natural(n-1)
# n = int(input("Enter a number : "))
# print(natural(n))

# Factorial 
def fact(n):
    if n < 0:       #Base condition
         return None     
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
n = int(input("Enter a number : "))
print(f"The factorial of {n} is {fact(n)}.")