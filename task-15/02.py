#!/bin/python3

import sys


t = int(input().strip())
for _ in range(t):
    n = int(input())
    a, b = 0, 1
    sum = 0
    for i in range(n):
        if(a>=n):
            break
        if (a % 2 == 0):
            sum =sum + a
        a, b = b, a + b
    print(sum)

