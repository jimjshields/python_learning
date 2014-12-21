def fib_orig(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_orig(n-1) + fib_orig(n-2)

print fib_orig(100)