def count_primes(n):
    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    prime_count = sum(is_prime)
    return prime_count

n = 500
print(f"Кількість простих чисел менших {n}: {count_primes(n)}")