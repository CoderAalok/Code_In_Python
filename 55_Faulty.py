
# while True:
#     num1 = int(input("Enter first number: ").strip())
#     num2 = int(input("Enter second number: ").strip())

#     print("Select any operator: (+), (-), (*), (/)")
#     operator = input().strip()
#     try:
#         if operator == '+':
#             if num1 == 90 and num2 == 45:
#                 print(f"The addition of {num1} {operator} {num2} = 999")
#             else:
#                 sum_num = num1 + num2
#                 print(f"The addition of {num1} {operator} {num2} = {sum_num}")
                
#         elif operator == '-':
#             if num1 == 69 and num2 == 100:
#                 print(f"The subtraction of {num1} {operator} {num2} = -9999")
#             else:
#                 sub_num = num1 - num2
#                 print(f"The subtraction of {num1} {operator} {num2} = {sub_num}")

#         elif operator == '*':
#             if num1 == 590 and num2 == 1000:
#                 print(f"The multiplication of {num1} {operator} {num2} = 9090")
#             else:
#                 mul_num = num1 * num2
#                 print(f"The multiplication of {num1} {operator} {num2} = {mul_num}")

#         elif operator == '/':
#             if num1 == 690 and num2 == 1005 :
#                 print(f"The division of {num1} {operator} {num2} = 0.9999")
#             else:
#                 div_num = num1 / num2
#                 print(f"The division of {num1} {operator} {num2} = {div_num}")
        
#         user = input("Calculation more (yes/no)?").strip().lower()
#         if user == "yes":
#             continue
#         else:
#             break
#     except (ValueError, ZeroDivisionError) as e:
#         print(e)
   
   
#  Command Line Utility: It is a software program that designed in this way which executed form a Command Line Interface(CLI) rather than GUI(Graphic User Interface).
# It perform a specific task and intracts with the user input and output.
# It is text based interaction. Standard input or input is provided command arguments, flags and output print on text form.
# Single responsibility: Each utility usually peforms one well defined task.(listing files, filtering text, copy data)
# Lightweight and fast than GUI. Fewer system resourses consume CLI
# Scriptable and automatable:CLI combined in scripts or chained together using pipes(|) and to build complex workflow
import argparse
import sys

def calculator(args):
    if not args:
        return
    if args.operator == '+':
        if args.num1 == 90 and args.num2 == 45:
            return (f"The addition of {args.num1} {args.operator} {args.num2} = 999")
        else:
            sum_num = args.num1 + args.num2
            return (f"The addition of {args.num1} {args.operator} {args.num2} = {sum_num}")
            
    elif args.operator == '-':
        if args.num1 == 69 and args.num2 == 100:
            return (f"The subtraction of {args.num1} {args.operator} {args.num2} = -9999")
        else:
            sub_num = args.num1 - args.num2
            return (f"The subtraction of {args.num1} {args.operator} {args.num2} = {sub_num}")

    elif args.operator == '*':
        if args.num1 == 590 and args.num2 == 1000:
            return (f"The multiplication of {args.num1} {args.operator} {args.num2} = 9090")
        else:
            mul_num = args.num1 * args.num2
            return (f"The multiplication of {args.num1} {args.operator} {args.num2} = {mul_num}")

    elif args.operator == '/':
        if args.num1 == 690 and args.num2 == 1005 :
            return (f"The division of {args.num1} {args.operator} {args.num2} = 0.9999")
        else:
            div_num = args.num1 / args.num2
            return (f"The division of {args.num1} {args.operator} {args.num2} = {div_num}")
    else:
        return ("Something went wrong.")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()  #creates a object
    
    parser.add_argument("num1", type=float, default=0, help="Number must be integer.")
    parser.add_argument("num2", type=float, default=0, help="Number must be integer.")
    parser.add_argument("operator", help="Operation like (+), (-), (*), (/)")
    
    
    args = parser.parse_args()
    sys.stdout.write(str(calculator(args)))
    
    
    
   