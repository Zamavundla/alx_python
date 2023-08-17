#! /usr/bin/python3
def is_prime(number):
    # If the number is less than or equal to 1, it's not prime, so return False.
    if number <= 1:
        return False

    # Check for divisors from 2 up to the square root of the number 
    # (rounded up to the nearest integer).
    # If the number is divisible by any of these divisors, 
    # it's not prime, so return False.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    # If the loop completes without finding any divisors,
    #the number is prime, so return True.
    return True

