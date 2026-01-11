# x = 40 
# def fun_global():
#     print(x)  #read global variable only
# fun_global()


x = 40 
def fun_global():
    global x
    # x *= 5
    print(x)  #read global variable  and modify by 'global' keyword 
fun_global()
print(x) 
