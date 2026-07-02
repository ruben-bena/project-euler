fibonacci_numbers = {
    1: 1,
    2: 2,
}

def fibonacci_of(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n in fibonacci_numbers.keys():
        return fibonacci_numbers[n]
    fibonacci = fibonacci_of(n-1) + fibonacci_of(n-2)
    fibonacci_numbers[n] = fibonacci
    return fibonacci

n = 1
current_fibonacci = 0
limit = 4000000
while current_fibonacci < limit:
    current_fibonacci = fibonacci_of(n)
    n += 1
del fibonacci_numbers[n-1] # Borra el último número de fibonacci calculado, ya que excede el límite
sum_of_all_even_fibonacci_below_limit = sum(list(filter(lambda n: n%2==0, fibonacci_numbers.values())))
print(f"La suma de todos los numeros de Fibonacci menores a 4.000.000 es...{sum_of_all_even_fibonacci_below_limit}")
