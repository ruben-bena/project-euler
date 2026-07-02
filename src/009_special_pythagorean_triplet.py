'''A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
                        a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a+b+c=1000.
Find the product abc.'''

def is_pythagorean_triplet(a:int, b:int, c:int) -> bool:
    return c**2 == a**2 + b**2

def find_special_pythagorean_triplet():
    for c in range(1, 1000):
        for b in range(1, c):
            for a in range(b, c):
                if is_pythagorean_triplet(a, b, c) and a+b+c==1000:
                    print(f"The pythagorean triplet was {a}² + {b}² = {c}²:")
                    print(f"a+b+c={a}+{b}+{c}=1000")
                    print(f"a·b·c={a}·{b}·{c}={a*b*c}")
                    return a*b*c
    print("The special pythagorean was not found :(")
    return -1

result = find_special_pythagorean_triplet()
print(f"The product of the special pythagorean triplet is...{result}")