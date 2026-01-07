<<<<<<< HEAD
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter  the second number: ")) 
operation = input("Enter the operation (+, -, *, / ,!): ")
if operation == '+':
    sum = num1 + num2
    print("The sum is:", sum)
elif operation == '-':      
    difference = num1 - num2
    print("The difference is:", difference)
elif operation == '*':
    product = num1 * num2
    print("The product is:", product)
elif operation == '/':
    if num2 != 0:
        quotient = num1 / num2
        print("The quotitent is :", quotient)
    else:
        print("Undifined cannot divide by zero")   
elif operation == '!':
    fact=1
    fact1=1
    if num1<0  and num2<0:
        print("Factorial is not defined for negative numbers")
    elif num1==0 or num1==1 and num2==0 or num2==1  :
        print(f"The factorial of {num1} and{num2} is 1")
    else:
        for i in range(1,num1 + 1):
            fact=fact*i
        print(f'The factorial of {num1} is:',fact)
        for j in range(1,num2 + 1):
            fact1 = fact1*j
        print(f'The factorial of {num2} is:',fact1)
        
=======
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter  the second number: ")) 
operation = input("Enter the operation (+, -, *, / ,!): ")
if operation == '+':
    sum = num1 + num2
    print("The sum is:", sum)
elif operation == '-':      
    difference = num1 - num2
    print("The difference is:", difference)
elif operation == '*':
    product = num1 * num2
    print("The product is:", product)
elif operation == '/':
    if num2 != 0:
        quotient = num1 / num2
        print("The quotitent is :", quotient)
    else:
        print("Undifined cannot divide by zero")   
elif operation == '!':
    fact=1
    fact1=1
    if num1<0  and num2<0:
        print("Factorial is not defined for negative numbers")
    elif num1==0 or num1==1 and num2==0 or num2==1  :
        print(f"The factorial of {num1} and{num2} is 1")
    else:
        for i in range(1,num1 + 1):
            fact=fact*i
        print(f'The factorial of {num1} is:',fact)
        for j in range(1,num2 + 1):
            fact1 = fact1*j
        print(f'The factorial of {num2} is:',fact1)
        
>>>>>>> aa2e7dcd15f91be88c03e886b9e67eae8692673b
