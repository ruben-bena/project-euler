def sum_all_multiples_of_three_or_five_until(number: int) -> int:
    return sum(list(filter(lambda n: n%3==0 or n%5==0, range(number))))

print(sum_all_multiples_of_three_or_five_until(10))
print(sum_all_multiples_of_three_or_five_until(1000))