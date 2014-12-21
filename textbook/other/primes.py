def is_prime(n):
    primes = dict()
    vals = primes.values()
    count = 0
    for n in range(1, n):
        for p in range(1, n):
            if n in vals:
                n += 1
            if n % p == 0:
                n += 1
            else:
                primes[count] = n
                count +=1
    print primes

is_prime(100)
        