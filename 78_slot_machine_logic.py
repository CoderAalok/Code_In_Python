class RandomGenerator:
    # Seed: Initial or stating value
    def __init__(self, seed=1):
        self.X = seed    # X -> State 
    
    def next(self):
        a = 1112233 # multiplier
        c = 1123 # Increment
        m = 2**31 # module
        
        self.X = (a * self.X + c) % m
        return self.X

class Biased(RandomGenerator):
    def random_biased(self):
        probabilities = (
            [1]*1 +
            [2]*2 +
            [3]*5 +
            [4]*2 +
            [5]*1 + 
            [6]*5
        )
        
        index = self.next() % len(probabilities)
        return probabilities[index]


rng = Biased(seed=123)
for _ in range(20):
    print(rng.random_biased())

import numpy
print(numpy.random.randint(low=1, high=6, size=20))


# LCGs = Linear Congurencial Generators
# Formula: Xₙ₊₁ = (a · Xₙ + c) mod m

# import random
# class RandomGenerator:
#     # Seed: Initial or stating value
#     def __init__(self, seed=1):
#         self.X = seed    # X -> State 
    
#     def next(self, a, c, m=2**31):
#         # a ->  # multiplier
#         # c -> # Increment
#         # m -> # module
        
#         self.X = (a * self.X + c) % m
#         return self.X

# class Biased(RandomGenerator):
#     def winning_chance(self):
#         probabilities = (
#             [1]*1 +
#             [2]*2 +
#             [3]*5 +
#             [4]*2 +
#             [5]*1 + 
#             [6]*5
#         )
        
#         prices = {
#             1:'$5',
#             2:'$1',
#             3:'$0',
#             4:'$1',
#             5:'$5',
#             6:'$0'
#         }
        
#         index = self.next(a, c) % len(probabilities)
#         n = probabilities[index]
#         return f"{prices[n]}"

# rng = Biased()

# a = random.randint(100, 100000)
# c = random.randint(100, 10000)
# rng.next(a, c)
# player = f"You won {rng.winning_chance()}"
#print(player)