import logging

FORMAT = ('%(asctime)s:%(levelname)s:%(message)s')

def factorial(n):
    logging.basicConfig(filename ="Factorial.log", level=logging.DEBUG, format=FORMAT)
    
    fact = 1
    for x in range(1, n+1):
        fact *= x
        # logging.debug(fact)
    return fact
n = 5
f = factorial(n)
logging.warning("Factorial:{} = {} ".format(n, f))