n = 10
found = False
f=1
for i in range(1,n+1):
    f=f*i

for num in range(n, f+1):
    d = True
    for i in range(1, n + 1):
        if num % i != 0:
            d = False
            break
    if d:
        found = True
        print( num)
        break
