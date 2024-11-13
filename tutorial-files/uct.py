#this file computes upper confidence bounds 
# for MCST

import math

def uct(op, q, n, parent_n):
    return (op * q) + math.sqrt(math.log(parent_n + 1) / (n+1))

#take user input and return uct value
while True:
    op = float(input("Min or Max: "))
    q = float(input("Q: "))
    n = float(input("N: "))
    parent_n = float(input("Parent N: "))
    print(uct(op, q, n, parent_n))


