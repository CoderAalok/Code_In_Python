

#solid Triangle

# size = 7
# for r in range(size):
#     for c in range(r,size):
#         print(' ',end='')
#     for c in range(r):
#         print('*',end='')
#     for c in range(r+1):
#         print('*',end='')
    
#     print()
    
#Solid Triangle
# size = 7
# for i in range(size):
#     for j in range(i,size):
#         print(' ',end='')
#     for j in range(i+1):
#         print('*', end=' ')
        
#        #Hollow triangle 
#         # if i == size-1 or j == i or j==0: 
#         #     print('*',end=' ')
#         # else:
#         #     print(' ',end=' ')
#     print()
    
# size = 7 
# for i in range(size):
#     for j in range(i+1):
#         print('-',end='')
#     for j in range(i,size):
#         print(chr(ord('a')+j), end='-') #with space
#     # for j in range(i+1,size):#without space
#     #     print('*', end='')
#     for k in range(i+1):
#         print('-',end='')
#     print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if j == 0 or  i+j == n-1  or i == 0:
#             print('*' , end=' ')
#         else:
#             print(' ', end=' ')
#     print()


n =  3
for i in range(n):
    
    for j in range(i,n):
        print("-",end=' ')
    
    for k in range(i):
        print(chr(ord('a')+k),end='-')
       
    for m in range(i+1):
        print(chr(ord('a')+m),end='-')
    
    for j in range(i,n):
        print("-",end=' ')
    print()
print("---Code Camp---")
for i in range(n):  
    for a in range(i):
        print(' ','-',end='')
    
    for r in range(i,n):
        print('',chr(ord('a')+r),end='-')
    
    for m in range(i,n-1):
        print('',chr(ord('a')+m),end='-') 
    print()


# #-=================================================================================================================  
# n = 7
# m = n*3

# # Top 
# for r in range(n//2):
#     pattern = '.|.'*(2*r+1)
#     print(pattern.center(m,"_"))

# # Middle
# print("WELCOME".center(m,"_"))

# # Bottom
# for r in range(n//2):
#     k = (n//2)-r
#     pattern = '.|.'*((2*k)-1)
#     print(pattern.center(m,"_"))
