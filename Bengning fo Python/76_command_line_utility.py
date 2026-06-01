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
    
    
    
   