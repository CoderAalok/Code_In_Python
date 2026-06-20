
while True:
    num1 = int(input("Enter first number: ").strip())
    num2 = int(input("Enter second number: ").strip())

    print("Select any operator: (+), (-), (*), (/)")
    operator = input().strip()
    try:
        if operator == '+':
            if num1 == 90 and num2 == 45:
                print(f"The addition of {num1} {operator} {num2} = 999")
            else:
                sum_num = num1 + num2
                print(f"The addition of {num1} {operator} {num2} = {sum_num}")
                
        elif operator == '-':
            if num1 == 69 and num2 == 100:
                print(f"The subtraction of {num1} {operator} {num2} = -9999")
            else:
                sub_num = num1 - num2
                print(f"The subtraction of {num1} {operator} {num2} = {sub_num}")

        elif operator == '*':
            if num1 == 590 and num2 == 1000:
                print(f"The multiplication of {num1} {operator} {num2} = 9090")
            else:
                mul_num = num1 * num2
                print(f"The multiplication of {num1} {operator} {num2} = {mul_num}")

        elif operator == '/':
            if num1 == 690 and num2 == 1005 :
                print(f"The division of {num1} {operator} {num2} = 0.9999")
            else:
                div_num = num1 / num2
                print(f"The division of {num1} {operator} {num2} = {div_num}")
        
        user = input("Calculation more (yes/no)?").strip().lower()
        if user == "yes":
            continue
        else:
            break
    except (ValueError, ZeroDivisionError) as e:
        print(e)
   
   
