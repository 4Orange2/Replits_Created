from copy import deepcopy

# This is the pattern for each for loop:
# use a for loop to determine the index of the first number
# remove that index as a possibility for all the other numbers
# use a for loop for the newly formed list to determine the index of the second number


def place_number(indexes, number):
  for index in indexes:
    print(f"this is {indexes}")
    if (number + 1) <= N:
      new_indexes = deepcopy(indexes)
      new_indexes.remove(index)
      print(f"this is modified {new_indexes}")
      print(f"this is original {indexes}")
      print("called place_number() again")
      place_number(new_indexes, number + 1)
    elif (number + 1) > N:
      print(one_to_N_list)
      print("going back in the recursion")


N = int(input("What is N? "))

one_to_N_list = list(range(1, N + 1))
indexes_of_num1 = list(range(N))

#for i in range(1, N + 1):
#  print("changing the position of number 1")

# place_number(indexes_of_num1, 1)

# More efficient method to solve the problem:

def place_at_index(ind, N):
  '''ind: the index to place the given number
  N: the number that the list of 1 to N is formed off of
  used: a list that just says whether the given index has been taken up or not (using boolean values)
  '''
  if ind >= N:
    print(one_to_N_list)
    return
  for i in range(N):
    if not used[i]:
      one_to_N_list[ind] = i
      used[i] = True
      #print(used)
      #print(f"this is {one_to_N_list}")
      place_at_index(ind+1, N)
      used[i] = False
      # next line is not necessary
      one_to_N_list[ind] = -1


used = [False]*N
one_to_N_list = [-1]*N
print(used)
print(one_to_N_list)
place_at_index(0, N)
