import math
from copy import deepcopy
# Arrange 1 to N in N! arrangements
# How to get away from the a bunch of loops
# Create a list of 1-N N times
  # Instead of doing a for i in range(), make the list beforehand and then remove() the element that you want to remove
# arrange, then make a list (which is going to be [1,2,3,4])
# 1 in first placeholder
  # 2 in second
  # 2 in third
  # 2 in fourth
  
# 1 in second placeholder
  # 2 in first
    
  # 2 in third
    # 3 in fourth
      # 1 
  # 2 in fourth

# 1 in third placeholder
  # 2 in first
    
  # 2 in second
  # 2 in fourth
# 1 in fouth placeholder
  # 2 in first
    # 3 in second
      # 4 in third
  # 2 in second
    # 3 in fouth
      # 4 in third
    # 3 in 
  # 2 in third
'''
# pseudocode:


'''

'''
one_to_N_list = list(range(1,5))
print(one_to_N_list)

def recursive_function(one_to_N_list):
  for num in one_to_N_list:
    print(num)
    one_to_N_list.remove(num)
    for i in one_to_N_list:
      print(i)
      one_to_N_list.remove(i)
      for a in one_to_N_list:
        print(a)
        one_to_N_list.remove(a)
        for e in one_to_N_list:
          print(e)
          print(f"{num}{i}{a}{e}")
          one_to_N_list.remove(e)

recursive_function(one_to_N_list)
'''
# the idea is that pos_1 represents the position of number 1
# pos_2 is position of number 2
'''
def list_modifier(one_to_N_list, index):
  new_list = deepcopy(one_to_N_list)
  new_list[index] =
  if :
    list_modifier(new_list, index - 1)
  elif :
    

one_to_N_list = list(range(1,4+1))
print(one_to_N_list)

for index in range(4):
''' 

one_to_4_list = list(range(1,5))
print(f"this is {one_to_4_list}")

# note: don't modify the for loop exit list in the for loop; it messes up the loop

# index_1; the position of the number 1 in the list

for index_1 in range(4):
  indexes = list(range(4))
  one_to_4_list[index_1] = 1
  print(f"this is {one_to_4_list}")
  print(indexes)
  indexes_2 = deepcopy(indexes)
  indexes_2.remove(index_1)
  print(f"this is indexes_2 {indexes_2}")
  for index_2 in indexes_2:
    print(f"this is i {index_2}")
    one_to_4_list[index_2] = 2
    print(f"this is indexes_3 {one_to_4_list}")
    indexes_3 = deepcopy(indexes_2)
    indexes_3.remove(index_2)
    print(f"this is indexes_3: {indexes_3}")
    print(f"this is indexes_2: {indexes_2}")
    for index_3 in indexes_3:
      print(f"this is indexes_3: {indexes_3}")
      print(f"this is one_to_4_list: {one_to_4_list}")
      one_to_4_list[index_3] = 3
      print(f"this is one_to_4_list {one_to_4_list}")
      indexes_4 = deepcopy(indexes_3)
      indexes_4.remove(index_3)
      for index_4 in indexes_4:
        print(f"THIS IS {indexes_4}")
        one_to_4_list[index_4] = 4
        print(f"FINAL LIST {one_to_4_list}")
