'''The sum of the primes below 10 is 2+3+5+7=17.

Find the sum of all the primes below two million.'''

from math import sqrt

def sum_of_primes_below_number(number: int) -> int:
    possible_primes = [True] * number
    primes = []
    limit = int(sqrt(number))
    for i, is_possible_prime in enumerate(possible_primes):
        prime_candidate = i+1
        if prime_candidate < 2:
            continue
        if not is_possible_prime:
            continue
        else:
            primes.append(prime_candidate)
            # Eliminar primos que sean múltiplos
            if prime_candidate > limit:
                continue
            counter = prime_candidate
            while prime_candidate * counter <= number:
                multiple_i = (prime_candidate * counter) - 1
                possible_primes[multiple_i] = False
                counter += 1
    return sum(primes)

numbers = [10, 2000000]
for number in numbers:
    print(f"The sum of primes below {number} is...{sum_of_primes_below_number(number)}")