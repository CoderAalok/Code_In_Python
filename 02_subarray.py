<<<<<<< HEAD
# arr = [2,4,5,7,8,9]
# k=12
# print("The first second index of the subarray are:  ")

def sub_array(arr,k):
    n = len(arr)
    sum = 0
    left = 0
    for right in range(n):
        sum += arr[right]
        while sum >k and right>=left:
            sum -= arr[left]
            left += 1
        if sum == k :
            return [left +1 ,right +1]
    return [-1]
arr = [3,2,3,4]#list(map(int,input('Enter the numbers  : ').split()))      #[2,4,5,7,8,9]
k  =  6#int(input('Enter a number :'))
result = sub_array(arr,k)
if result != [-1]:
    print("The first second index of the subarray are:  ",result)
else:
=======
# arr = [2,4,5,7,8,9]
# k=12
# print("The first second index of the subarray are:  ")

def sub_array(arr,k):
    n = len(arr)
    sum = 0
    left = 0
    for right in range(n):
        sum += arr[right]
        while sum >k and right>=left:
            sum -= arr[left]
            left += 1
        if sum == k :
            return [left +1 ,right +1]
    return [-1]
arr = [3,2,3,4]#list(map(int,input('Enter the numbers  : ').split()))      #[2,4,5,7,8,9]
k  =  6#int(input('Enter a number :'))
result = sub_array(arr,k)
if result != [-1]:
    print("The first second index of the subarray are:  ",result)
else:
>>>>>>> aa2e7dcd15f91be88c03e886b9e67eae8692673b
    print("No subarray exists.",result)