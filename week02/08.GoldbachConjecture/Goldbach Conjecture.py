def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            primes.append(i)
    return primes

#print(prime_numbers(7))


def goldbach(n):
    prime_nums = prime_numbers(n)
    result = []

    for i in prime_nums:
        j = i
        for i in prime_nums:
            if i + j == n:
                if (j, i) in result or (i, j) in result:
                    break
                else:
                    if i > j:
                        result.append((j, i))
                    else:
                        result.append((i, j))

    return result

print(goldbach(100))
