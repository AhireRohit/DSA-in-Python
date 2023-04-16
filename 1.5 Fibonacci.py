# Fibonacci sequence is a sequence of number in which each number is the sum of he twopreceding ones and sequence starts from 0 and 1.

def fibonacci(n):
    assert n >= 0 and int(n) == n, "Number should be positive"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(7))