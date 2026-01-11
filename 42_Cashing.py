
# lru_cache is use to improve better performance and avoid repeated computation of the same result

from functools import lru_cache 
import time
@lru_cache(maxsize=9999) # It retrieve the return data
def calculation_larger_number(n1, n2):
    time.sleep(2) # --> Assume a large program
    return n1 * n2

for _ in range(10):
    print(calculation_larger_number(12, 10))
    
print("Done")


