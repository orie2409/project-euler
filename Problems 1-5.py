import numpy as np
import pandas as pd


# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(n, a, b):
    # Sums all multiples of a or b for numbers below n.
    multiples_sum = 0
    for i in range(1, n):
        if i % a == 0 or i % b == 0:
            multiples_sum = multiples_sum + i
    return multiples_sum


print(multiples(10, 3, 5))
print(multiples(1000, 3, 5))


# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci_even_sum(n):
    i = 1
    j = 2
    sum_even = 0
    while j < n:
        if j % 2 == 0:
            sum_even = sum_even + j
        j1 = i + j
        i = j
        j = j1
    return sum_even


print(fibonacci_even_sum(4000000))


# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def prime_factors(n):
    # Stores all prime factors in a list
    prime_factor_list = []
    m = 2
    while n > 1:
        if n % m == 0:
            prime_factor_list.append(m)
            n = n / m
        else:
            m = m + 1
    return prime_factor_list


def max_prime(n):
    # Returns the maximum of the values in array of prime numbers using NumPy amax
    a = prime_factors(n)
    return np.amax(a)

print(max_prime(600851475143))

# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

debug = False


def max_palindrome():
    # Returns maximum palindrome for products of two 3-digit numbers.
    palindrome_list = []
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            debug and print(i)
            debug and print(j)
            k1 = i*j
            k2 = str(k1)
            if (k2[0] == k2[-1] and k2[1] == k2[-2] and k2[2] == k2[-3] and len(k2) == 6) or \
                    (k2[0] == k2[-1] and k2[1] == k2[-2] and len(k2) == 5):
                palindrome_list.append(k1)
    return np.amax(palindrome_list)

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. LCM
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Counter allows set operations for lists containing non-unique elements.
from collections import Counter as mset

def prime_factors(n):
    # Stores all prime factors in a list
    prime_factor_list = []
    m = 2
    while n > 1:
        if n % m == 0:
            prime_factor_list.append(m)
            n = n / m
        else:
            m = m + 1
    return prime_factor_list

debug = False

def find_lcm(n):
    # Finds the lowest common multiple for integers 1 through n
    lcm_list = []
    for i in range(2, n+1):
        debug and print(i)
        prime_list = prime_factors(i)
        debug and print(prime_list)
        a = mset(prime_list)
        b = mset(lcm_list)

        intersect_list = a & b
        debug and print(intersect_list)
        to_append_list = a - intersect_list
        lcm_list.extend(list(to_append_list.elements()))
        debug and print(to_append_list)
        debug and print(lcm_list)
    return print(np.product(lcm_list))

find_lcm(10)
find_lcm(20)
