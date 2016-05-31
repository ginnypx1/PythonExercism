def sieve(x):
    primes = []
    not_prime = [False] * (x+1)

    for i in range(2, (x+1)):
        if not_prime[i]:
            continue
        for f in range(i*2, (x+1), i):
            not_prime[f] = True

        primes.append(i)

    return primes

if __name__ == '__main__':
  print(sieve(1000))