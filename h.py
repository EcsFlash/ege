def primes():
    def is_odd_prime(n):
        if n % 3 == 0: return False
        i, w = 5, 2
        while i * i <= n:
            if n % i == 0: return False
            i += w
            w = 6 - w
        return True

    n, w = 5, 2
    yield from (2, 3, n)
    while True:
        n += w
        if n < 25 or is_odd_prime(n): yield n
        w = 6 - w


def prime_facts(n):
    for p in primes():
        if n < p * p: break
        t = n
        while t % p == 0:
            t //= p
            yield p


def facts(n):
    dd, tt = [1], []
    for p in primes():
        if n < p * p: break
        t, e = n, 1
        while t % p == 0:
            tt += [d * p ** e for d in dd]
            t //= p
            e += 1
        if e > 1:
            dd += tt
            del tt[:]
    if n != dd[-1]:
        dd += [n // d for d in dd]
    return sorted(dd)