# Find the length of anumber without using the length function

from math import *

number_str = (input("Enter the number that you want to find the length of? "))

full_number = int(number_str)
print(full_number)

exclude_last_digit = int(number_str[1:])
print(exclude_last_digit)

length = log(a=(full_number - exclude_last_digit), Base=10)

print(length)
