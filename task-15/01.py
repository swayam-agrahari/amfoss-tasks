t = int(input().strip())

for _ in range(t):
    n = int(input()) - 1  # Since we want multiples below n

    sum_3 = 3 * (n // 3) * ((n // 3) + 1) // 2
    sum_5 = 5 * (n // 5) * ((n // 5) + 1) // 2
    sum_15 = 15 * (n // 15) * ((n // 15) + 1) // 2

    total_sum = sum_3 + sum_5 - sum_15
    print(total_sum)
