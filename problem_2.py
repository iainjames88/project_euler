def fib(n):
    old, curr = 0, 1
    while curr <= n:
        old, curr = curr, curr + old
        yield curr

print(sum(x for x in fib(4000000) if x % 2 == 0))
