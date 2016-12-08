def fib(n):
    if n == 1 or n == 0:
        cache[n] = 1
        return cache[n]
    if n - 1 in cache and n - 2 in cache:
        cache[n] = cache[n - 1] + cache[n - 2]
    else:
        cache[n] = fib(n - 1) + fib(n -2)
    return cache[n]


cache = {}
num = 10
print fib(num)
print cache
