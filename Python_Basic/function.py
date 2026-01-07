
# def fun(a,b):
#     return a+b
# print(fun(4))

# def fun(a, b=0):
#     return a+b
# f = fun(b=9,a=9)  # This is clearlify order is  not matter in that case only else it matter positional keyword arguments!
# print(f)


# import random
# def fun(a, b=random.randint(1,5)):
#     return a*b
# print(fun(5))
    

# def fun(size,mess):
#     print(f"The size of T-shirt large_size is {size} and {mess}")
#     # return [size , mess]
# mess = "It's price is too execlusive only $40"
# size = 32
# fun(size,mess)
# fun(size=34,mess='We are welcome to Python store!')
# # print(f" and it cost {fun(size,mess)}")
while True:
    try:
        num_1 = int(input("Enter first Number: "))
        num_2 = int(input("Enter second Number: "))
        sum_num = num_1 + num_2
        print(f"The sum of {num_1} and {num_2}: {sum_num}")
        more = input("Adding more (yes/no)").lower().strip()
        if more == 'yes':
            continue
        elif more == 'no':
            break
        else:
            print("Over write! Either (yes/no) only.")
            continue
    except ValueError: 
        print("Please! Enter Numbers...")
        continue