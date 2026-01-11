num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number:" ))
num4 = int(input("Enter fourth number: "))
print(max(num1,num2,num3))
if num1 > num2:
    result = num1
else:
    result = num2
if num3 > num4:
    result1 = num3
else:
    result1 = num4
if result > result1:
    print(f'The greatest number is {result}')
else:
    print(f'The greatest number is {result1}')
    