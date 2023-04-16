# import sys
# sys.setrecursionlimit(10000)


def factorial(n):
    assert n>=1 and int(n)==n, "Positive numbers only!"
    if n in [0, 1]:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))