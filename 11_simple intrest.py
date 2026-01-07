def comp(a,p,r,t):
    a = p*(1+ (r/100))**t
    result = a - p
    return result
print(comp(a=2 , p =5 , r=4, t=2))