def is_palindrome(number: int) -> bool:
    return str(number)[::-1] == str(number)

def find_larges_palindrome_product_from_numbers_with_these_digits(n_digits: int) -> int:
    lowest_number = 10 ** (n_digits-1)
    highest_number = 10 ** n_digits
    current_biggest_palindrome = 0
    for i in range(lowest_number, highest_number):
        for j in range(lowest_number, highest_number):
            value = i*j
            if is_palindrome(value) and value > current_biggest_palindrome:
                current_biggest_palindrome = value
    return current_biggest_palindrome

print(find_larges_palindrome_product_from_numbers_with_these_digits(2))
print(find_larges_palindrome_product_from_numbers_with_these_digits(3))