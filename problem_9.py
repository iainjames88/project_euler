def is_prime(n):
    for i in range(n, -1, -1):
        print(i)

print(sum(x for x in range(0, 10) if is_prime(x)))
