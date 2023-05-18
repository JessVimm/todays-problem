# EXERCISE 8:           Prime Numbers
# Problem Statement:    Create a function calc_primes_up_to(max_value) to
#                       compute all prime numbers up to a given value.

def is_prime(number):

    for num in range(2, number):
        if number % num == 0:
            return False
    return True

value = int(input("Enter a natural number: "))

prime_numbers = []

if value >= 2:
    
    for num in range(2, value):
        if is_prime(num):
            prime_numbers.append(num)

print(prime_numbers)

