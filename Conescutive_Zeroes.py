# takes a string of zeroes and ones as an input and returns the largest number of consecutive zeroes in that string

print(len([0]))

binary_digits = input('Enter your string of binary digits: ')

binary_digits = binary_digits + "1"

# function to identify all consecutive zeroes of a string

def longest_element_in_list(list):
  print(f"this is our list: {list}")
  longest_occurence = len([])
  for element in list:
    print(f"this is our element {element}")
    if len(element) > longest_occurence: 
      longest_occurence = len(element)  
  return longest_occurence
    
  

def zeroes_in_binary_digit(binary_digits):
  zeroes_list = []
  consecutive_zeroes = []
  previous_digit = 1
  for index in range(len(binary_digits)):
    digit = int(binary_digits[index])
    print(consecutive_zeroes)
    if index != 0:
      previous_digit = int(binary_digits[index-1])
    if digit == 0:
      consecutive_zeroes.append(digit)
    elif digit == 1 and previous_digit == 0:
      print(zeroes_list)
      zeroes_list.append(consecutive_zeroes)
      consecutive_zeroes = []
    else:
      pass
  longest_occurence = longest_element_in_list(zeroes_list)
  return longest_occurence


print(f"{zeroes_in_binary_digit(binary_digits)} consecutive zeroes")
"00010110000110010110100000010011001"