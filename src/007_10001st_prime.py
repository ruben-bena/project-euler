"""By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

from math import isqrt

def is_prime(prime_candidate: int, current_primes: list) -> bool:
    max_value = isqrt(prime_candidate)
    for prime in current_primes:
        if prime > max_value:
            return True
        if prime_candidate % prime == 0:
            return False
    return True

def find_prime_number(prime_number: int):
    primes = []
    prime_candidate = 2
    while len(primes) < prime_number:
        if is_prime(prime_candidate, primes):
            primes.append(prime_candidate)
        prime_candidate += 1
    return primes[-1]

prime_numbers = [6, 10001]
for prime_number in prime_numbers:
    print(f"The {prime_number}st prime is...{find_prime_number(prime_number)}")