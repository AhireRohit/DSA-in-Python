def sum(n):
    n = int(n)
    assert n >= 0 and int(n) == n, "Use positive numbers only!"
    if n < 10:
        return n
    else:
        return n%10 + sum(n/10)

print(sum(112))