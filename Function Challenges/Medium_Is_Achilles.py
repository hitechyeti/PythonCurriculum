def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors_with_exponents(n):
    factors = {}
    i = 2
    while i * i <= n:
        while (n % i) == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors

def is_powerful(n):
    factors = prime_factors_with_exponents(n)
    return all(exp >= 2 for exp in factors.values())

def is_perfect_power(n):
    for i in range(2, int(n ** 0.5) + 1):
        power = i * i
        while power <= n:
            if power == n:
                return True
            power *= i
    return False

def is_achilles(n):
    if is_powerful(n) and not is_perfect_power(n):
        return True
    return False
