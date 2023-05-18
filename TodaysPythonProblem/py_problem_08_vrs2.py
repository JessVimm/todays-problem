# EXERCISE 8:           Prime Numbers
# Problem Statement:    Create a function calc_primes_up_to(max_value) to
#                       compute all prime numbers up to a given value.
# This is solved following the Sieve of Eratosthenes Algorithm.

def calc_primes_up_to(max_value):
    # Set all numbers to be potentially primes
    potentially_primes = [True for _ in range(0,max_value + 1)]

    # Check if each value is prime
    for number in range(2, max_value // 2 + 1):
        # If prime, delete all its multiples
        if potentially_primes[number]:
            delete_multiples_of(number, potentially_primes)

    return generate_prime_list(potentially_primes)


def delete_multiples_of(number, current_primes):
    for multiple in range(number + number, len(current_primes), number):
        current_primes[multiple] = False    

def generate_prime_list(prime_list):
    final_primes = []
    for number in range(2, len(prime_list)):
        if prime_list[number]:
            final_primes.append(number)
    return final_primes


value = int(input("Enter a natural number: "))

prime_numbers = calc_primes_up_to(value)
print(prime_numbers)

