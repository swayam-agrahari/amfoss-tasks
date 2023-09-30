#!/bin/python3

import sys
import math
t = int(input().strip())

def l(n):
    prime = -1
    
    while n % 2 == 0:
        prime = 2
        n //= 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime = i
            n //= i
    
    if n > 2:
        prime = n
    
    return prime

t = int(input("").strip())
for _ in range(t):
    n = int(input(""))
    result = l(n)
    print(result)

