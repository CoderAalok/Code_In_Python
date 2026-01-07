# Problem:  Find the sum of n natural number which divisible by 3 or 5(a or b)

# Number of test execute
t = int(input().strip())

for _ in range(t):
    N = int(input().strip())
    # k = int(input().strip())
    N -= 1
    
    def sumNumber(k):
        m = N//k
        ans = k*m*(m+1)//2
        return ans
    result = sumNumber(3) + sumNumber(5) - sumNumber(15)#->> twice avoid ((a) + (b) - (a*b))
    print(result)
    
    
def sum_natural(n, k):
    n = (n)//k
    sum_N = k*(n*(n+1))//2
    return sum_N

# No. of test
test = int(input()) 


for _ in range(test):
    # n -> Natural number
    n = int(input().strip())
    # k -> Divisible number
    # k = int(input().strip())
    
    total_sum = sum_natural(n, 3) + sum_natural(n, 5) - sum_natural(n, 15)
    print(total_sum)