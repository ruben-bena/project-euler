"""The following iterative sequence is defined for the set of positive integers:

    n -> n/2    (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem), it is 
thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

def collatz_sequence_length_for_number(number: int, collatz_lengths: dict) -> int:
    if number == 1:
        return 1
    if number in collatz_lengths.keys():
        return collatz_lengths[number]
    is_even = number % 2 == 0
    if is_even:
        next_number = number / 2
    else:
        next_number = 3 * number + 1
    return collatz_sequence_length_for_number(next_number, collatz_lengths) + 1

def find_longest_collatz_sequence_number_until(limit: int) -> int:
    collatz_lengths = {}
    for number in range(2, limit):
        collatz_lengths[number] = collatz_sequence_length_for_number(number, collatz_lengths)
    # print(collatz_lengths[13]) -> Should be 10
    return max(collatz_lengths, key=collatz_lengths.get)
    
limit = 1000000
print(f"The number under {limit} that produces the longest collatz sequence is...{find_longest_collatz_sequence_number_until(limit)}")