"""Utilities for primality checks and listing primes below a number.

Run as a script to print whether N is prime and all primes less than N.
"""

import sys
from math import isqrt


def is_prime(n: int) -> bool:
    """Return True if n is prime, else False (handles n <= 1)."""
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3
    if n % 2 == 0:
        return False
    # check odd divisors up to sqrt(n)
    limit = isqrt(n)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True


def primes_below(n: int) -> list[int]:
    """Return a list of all prime numbers < n using the Sieve of Eratosthenes."""
    if n <= 2:
        return []
    sieve = bytearray(b"\x01") * n  # True-ish for indices 0..n-1
    sieve[0:2] = b"\x00\x00"        # 0 and 1 are not prime
    limit = isqrt(n - 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n:step] = b"\x00" * ((n - 1 - start) // step + 1)
    return [i for i in range(2, n) if sieve[i]]


def main() -> None:
    """CLI entrypoint: parse N and print primality plus primes below N."""
    # Accept either command-line arg or interactive input
    if len(sys.argv) == 2:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Please provide an integer, e.g. `python prime.py 37`.")
            return
    else:
        try:
            n = int(input("Enter an integer: ").strip())
        except ValueError:
            print("Please enter a valid integer.")
            return

    prime_flag = is_prime(n)
    print(f"{n} is {'a prime' if prime_flag else 'not a prime'} number.")
    below = primes_below(n)
    if below:
        print(f"Primes less than {n} ({len(below)} total):")
        print(", ".join(map(str, below)))
    else:
        print(f"No primes exist below {n}.")


if __name__ == "__main__":
    main()
