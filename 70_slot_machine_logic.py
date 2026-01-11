# class RandomGenerator:
#     # Seed: Initial or stating value
#     def __init__(self, seed=1):
#         self.X = seed    # X -> State 
    
#     def next(self):
#         a = 1112233 # multiplier
#         c = 1123 # Increment
#         m = 2**31 # module
        
#         self.X = (a * self.X + c) % m
#         return self.X

# class Biased(RandomGenerator):
#     def random_biased(self):
#         probabilities = (
#             [1]*1 +
#             [2]*2 +
#             [3]*5 +
#             [4]*2 +
#             [5]*1 + 
#             [6]*5
#         )
        
#         index = self.next() % len(probabilities)
#         return probabilities[index]


# rng = Biased(seed=123)
# for _ in range(20):
#     print(rng.random_biased())

# import numpy
# print(numpy.random.randint(low=1, high=6, size=20))


# LCGs = Linear Congurencial Generators
# Formula: Xₙ₊₁ = (a · Xₙ + c) mod m


import re


def winning_chance(money, n):
    probabilities = (
        [1]*3 +
        [2]*2 +
        [3]*10 +
        [4]*3 +
        [5]*2 + 
        [6]*10
    )
    
    prices = {
        1:8,
        2:4,
        3:0,
        4:2,
        5:5,
        6:0
    }
    
    return  (prices[probabilities[n]] * money)

print("Let's play cash wining game...")
while True:
    print("NOTE: Exit for 'q'")
    user = (input("Add your bet amount: "))
    if user == 'q':
        break
    if user != 'q' and user.isdigit():
        
        guess = (input("Select any number [1-30]: "))
        pattern = re.compile(r"^[a-zA-Z!@#$%^''&-+=/)(}{;:.,|*]+$")
        if pattern.search(guess):
            print("Guess correct card number.")
            
        else:
            check = winning_chance(int(user), int(guess))
            print(f"You won ${check}.")
        
    else:
        print("Incorrect input.")

