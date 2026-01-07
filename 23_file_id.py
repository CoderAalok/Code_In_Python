def missing(arr):
    sum1 = 0
    q= len(arr)
    i = 0
    while i< q : 
        sum1 += arr[i] 
        i += 1
    #arr_sum = sum(arr)
    n = arr[q-1]
    m = arr[0] - 1
    net_sum = (n*(n+1)//2) - (m*(m+1)//2)
    return net_sum - sum1
arr = [20,21,22,24,25]
print(f' {missing(arr)} is missing element.')