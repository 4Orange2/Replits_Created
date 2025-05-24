from math import *
# this program prime factorizes a number
# we use the realization that it's enough to test for al numbers up to the square root of a number

number = 500

def determine_prime_roots(number):
  prime_factors = []
  while number%2 == 0:
    prime_factors.append(2)
    number /= 2
  for i in range(3, int(sqrt(number)), 2):
    if number%i ==0:
      prime_factors.append(i)
      number /= i
  return prime_factors

print(determine_prime_roots(number))