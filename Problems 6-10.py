# Problem 6: Sum of Squares

import numpy as np
import pandas as pd


def sum_squares_diff(n):
    sum_squares = 0
    square_sum = 0
    for i in range(1, n+1):
        sum_squares = sum_squares + i**2
        # print("For iteration %d sum_squares is: %d" % (i, sum_squares))
        square_sum = square_sum + i
    square_sum = square_sum**2
    return print(square_sum - sum_squares)

sum_squares_diff(10)
sum_squares_diff(100)

# Problem 7: nth prime number

import numpy as np
import pandas as pd


def is_prime(n):
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

is_prime(50)

# From the asymptotic law of prime numbers, the prime-counting function f(x) ~ x/log(x) as x~inf gives the density.
# Equivalently, p(n) ~ n log(n). I have multiplied by 2 to give additional allowance.
# find_nth_prime(n):


def find_nth_prime(n):
    prime_factor_list = []
    upper = int(round(2*n*np.log(n), 0))
    for i in range(1, upper):
        if is_prime(i):
            prime_factor_list.append(i)
    return prime_factor_list[n]

find_nth_prime(10001)
# Answer = 104743


# Problem 8: Maximum product of n adjacent digits.

a1 = '3677432'
debug = True

def max_product(a, n=2):
    products = []
    digits = []
    for i in range(0, len(a)-n+1):
        b = 1
        digits2 = []
        for j in range(0, n):
            b = b*int(a[i+j])
            digits2.append(int(a[i+j]))
        products.append(b)
        digits.append(digits2)
    max_val = np.amax(products)
    max_digits = digits[np.argmax(products)]
    return print('The maximum product of %d digits is %d with digits:' %(n,max_val),max_digits)

max_product(a1, 2)

a2 = '73167176531330624919225119674426574742355349194934' \
     '96983520312774506326239578318016984801869478851843' \
     '85861560789112949495459501737958331952853208805511' \
     '12540698747158523863050715693290963295227443043557' \
     '66896648950445244523161731856403098711121722383113' \
     '62229893423380308135336276614282806444486645238749' \ 
     '30358907296290491560440772390713810515859307960866' \
     '70172427121883998797908792274921901699720888093776' \
     '65727333001053367881220235421809751254540594752243' \
     '52584907711670556013604839586446706324415722155397' \
     '53697817977846174064955149290862569321978468622482' \
     '83972241375657056057490261407972968652414535100474' \
     '82166370484403199890008895243450658541227588666881' \
     '16427171479924442928230863465674813919123162824586' \
     '17866458359124566529476545682848912883142607690042' \
     '24219022671055626321111109370544217506941658960408' \
     '07198403850962455444362981230987879927244284909188' \
     '84580156166097919133875499200524063689912560717606' \
     '05886116467109405077541002256983155200055935729725' \
     '71636269561882670428252483600823257530420752963450'

max_product(a2, 4)
max_product(a2,13)
# Answer: The maximum product of 13 digits is 23514624000 with digits: [5, 5, 7, 6, 6, 8, 9, 6, 6, 4, 8, 9, 5]

# Question 9: Pythagorean Triplets


# Step 1: Create function to test is_pythagorean_triple
def is_pythagorean_triple(a,b,c):
    if a**2+b**2 == c**2:
        return True
    else:
        return False

is_pythagorean_triple(3,4,6)


# Step 2: Create function which runs through a,b,c and tests
def pythagorean_result(n):
    for a in range(1,n-1):
        for b in range(a+1,n-1):
            c = n-a-b
            if is_pythagorean_triple(a,b,c):
                return a,b,c,a*b*c


pythagorean_result(1000)
# Answer = (200, 375, 425, 31875000)

# Question 10: Sum of primes below x

def sum_nth_prime(n):
    prime_list = []
    for i in range(2, n):
        if is_prime(i):
            prime_list.append(i)
    return sum(prime_list)

sum_nth_prime(10)
sum_nth_prime(2000000)
# Answer = 