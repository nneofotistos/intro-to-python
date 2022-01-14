from locale import D_FMT
from socketserver import DatagramRequestHandler


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print('2', is_prime(2))
print('1693', is_prime(1693))
print('15', is_prime(15))
print('303212', is_prime(303212))
print('7', is_prime(7))
print('0', is_prime(0))

def first_n_primes(n):
    result = []
    num = 2
    if n == 0:
        return result
    while len(result) < n:
        if is_prime(num):
            result.append(num)
        num += 1
    return result

print('0', first_n_primes(0))
print('1', first_n_primes(1))
print('4', first_n_primes(4))
print('6', first_n_primes(6))
print('15', first_n_primes(15))

def sum_of_n_primes(n):
    arr = first_n_primes(n)
    result = 0
    if len(arr) == 0:
        return 0

    for number in arr:
        result += number

    return result

print('0', sum_of_n_primes(0))
print('1', sum_of_n_primes(1))
print('4', sum_of_n_primes(4))
print('6', sum_of_n_primes(6))
print('15', sum_of_n_primes(15))