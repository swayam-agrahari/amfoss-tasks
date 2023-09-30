#!/bin/python3

import sys

def palindrome(s):
    return s == s[::-1] 
    
def largest(n):
    ans = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            p = i * j
            if p < n and palindrome(str(p)) and p > ans:
                ans = p
            elif p < ans:
                break
    return ans

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    result = largest(n)
    print(result)

