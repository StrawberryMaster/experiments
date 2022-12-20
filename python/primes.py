def find_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

def main():
    n = 100
    primes = find_primes(n)
    print(f"The prime numbers between 2 and {n} are: {primes}")

if __name__ == "__main__":
    main()