MrSegersIQ = [120, 65, 101, 7, 1057, 855, 17]

# how to identify the biggest number out of an unsorted list

largest_number = 0

for element in MrSegersIQ:
  if element > largest_number:
    largest_number = element

print(largest_number)

# Problem: double all the numbers
# you need to actually double the numbers themselves

for i in range(len(MrSegersIQ)):
  MrSegersIQ[i] = MrSegersIQ[i] * 2 # this is how to modify the indexes of a list

print(MrSegersIQ)
  