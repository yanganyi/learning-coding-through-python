
# input:  1 2 3 4 5 6  7  8
# output: 1 1 2 3 5 8 13 21

def fib_slow(n):
    if n <= 1:
        return n
    else:
        return (fib_fast(n - 1) + fib_fast(n - 2))

def fib_fast(n):
    if n <= 1:
        return n

    results = [1] * n
    for i in range(2,n):
        results[i] = results[i-1] + results[i-2]
    return results[n-1]


print(fib_fast(1))
print(fib_fast(2))
print(fib_fast(3))
print(fib_fast(4))
print(fib_fast(5))
print(fib_fast(6))
print(fib_fast(7))

# takes less than 1 second
print(fib_fast(100))

# takes forever
# print(fib_slow(100))


