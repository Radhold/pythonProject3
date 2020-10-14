def prime(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    if counter > 2:
        return 'Составное число'
    elif counter == 2:
        return 'Простое число'


print(prime(0))
print(prime(1))
print(prime(2))
print(prime(3))
print(prime(4))
