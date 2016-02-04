def get_numbers():
    for a in range (800, 1000):
        for b in range(a, 1000):
            yield a * b

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(max(x for x in get_numbers() if is_palindrome(x)))
