


#def sub_array(arr, target):
#         z=len(arr)
#         sum=0
#         left=0
#         for right in range(z):
#                 sum+=arr[right]
#         while sum> target and right>=left:
#                   sum-= arr[right]
#         if sum==target:
#                  return [left+1 , right+1]
#                  
#         return [-1]
#            



#Phone number generator

#import random
#a=0,1,2,3,4,5,6,7,8,9
#phone=random.sample(a,8)

#print("  The phone number is +977 9 8",end="")

#for i in reversed(phone):
#   print("",i,end="")

#SUBARRAY....

#def sub_array(arr , target):
#    z=len(arr)
#    left=0
#    right=0
#    sum=0
#    for i in range(z):
#       right=i
#       sum+=arr[i]
#    while sum>target and right>= left:
#        sum-=arr[i]
#        left+=1
#        
#    if sum==target:
#        return [left+1, right+1]
#    return [-1]

#arr=[2,4,6,8]
#target= int(input("Enter a targeted number : "))
#print(sub_array(arr,target))


#def  sub_array(arr,target):
#  
#  for i in range(len(arr)):
#       sum=0
#       for j in range(i,len(arr)):
#            sum+=arr[j]
#            if sum ==target:
#                return [i+1,j+1]
#  return [-1]
#    
#arr=[2,4,6,8]
#target= int(input("Enter a targeted number : "))  

#if sub_array(arr,target) ==[-1]:
#   print(f"There is no subarray of {target}")
#else:
#   print(f"The subarray of {target} from", sub_array(arr,target))


#def duck(arg):
#    iter(arg)
#    return True
#     
# 
#print(duck("the pythonic is best to understand about code writting way"))
#     

#x="4579"
#if not isinstance(x,int) :
#  print(set(x)

#att=["Control jack","data access","cyber alert", "Networking","Quantum_computing"]
#val=[x for x in att if len(x)>11]
#print(val)

#val=None
#print(val)

#s=(2,5,7)
#if s :
#    print(f"some element inside{ s}")
#   
#unicode_string = "python"
#byte_string = unicode_string.encode("utf-8")
#print(byte_string) 
#print(byte_string.decode())


#for i in range(13):
# pass
#x=90
#print(x==0)


#def fun(arg):
#       if arg != int(arg):
#          return True
#       return None
#   
#   
#try:
#    arg=input("Enter a num..")
#    print(fun(arg))   
#except ValueError:
#     print("None")

#def f(a):
#    try :
#       return float(a)
#    except :
#        return None
#        
#a=input("numb..")       
#print(f(a) )
#        

#for i in range(10000):
#   print(i)


#s="Dynamic reference 12334"
#for i in s:
#    print(i, end="")

#q="Magnified "
#z=(iter(q))
#print(next(z))#and so on to iterate..

#q=input("type..")
#z=(isinstance(q,(int,float)))

#print(z, f"Input type is {type(q)}")

