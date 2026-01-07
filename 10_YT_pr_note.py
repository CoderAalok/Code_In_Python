# P = int(input("Enter principle : "))
# T = int(input("Enter time: "))
# R = int(input("Enter rate% : "))
# result = (P*T*R)/100
# print(f"The final amount is {result}")

def sim(P,T,R):
    return (P*T*R)/100
P ,T , R = 100,2,3
# P = 120000
# T = 2
# R = 4
print(sim(P,T,R))