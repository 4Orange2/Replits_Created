# sort given integer from low to high and then from high to low
# subtracts the (low_to_high) from the (high_to_low) to get the difference
# does this until we reach 6174

def int_to_array(integer):
  integer = str(integer)
  integer_array = []
  for i in range(len(integer)):
    integer_array.append(integer[i])
  return integer_array

def array_to_int(array):
  int_string = ""
  for digit in array:
    int_string += (str(digit))
  integer = int(int_string)
  return integer

integer = input("what is your integer that you want to test? ")
print(f"this is integer {integer}")
difference = integer

integer_array = []

# loop to form the array
  
while difference != 6174:
  integer_array = int_to_array(difference)
  low_to_high = sorted(integer_array)
  print(low_to_high)
  high_to_low = sorted(integer_array, reverse=True)
  print(high_to_low)
  difference = array_to_int(high_to_low) - array_to_int(low_to_high)
  print(difference)
  