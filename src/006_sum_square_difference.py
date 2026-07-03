"""The sum of the squares of the first ten natural numbers is,

1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sum_of_squares_until(number: int) -> int:
    sum_of_squares = 0
    for n in range(1, number+1):
        sum_of_squares += n*n
    return sum_of_squares

def square_of_sum_until(number: int) -> int:
    square_of_sum = 0
    for n in range(1, number+1):
        square_of_sum += n
    return square_of_sum * square_of_sum

numbers = [10, 100]
for number in numbers:
    sum_of_squares = sum_of_squares_until(number)
    square_of_sum  = square_of_sum_until(number)
    print(f"The difference between the square-of-sum ({square_of_sum}) and the sum-of-squares ({sum_of_squares}) of the first {number}th natural numbers is...{square_of_sum - sum_of_squares}")