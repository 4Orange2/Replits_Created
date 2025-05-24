temps = [-5, -2, 0, 0, 1, 4, 5, 3, 6, 5, 6, 7, 10, 13, 12, 11, 11, 8, 10, 7, 4, 0, -6, -3]

smallest_number = temps[0]
largest_number = 0

for element in temps:
  if element > largest_number:
    largest_number = element
  elif element < smallest_number: 
    smallest_number = element

print(f"this is the largest element: {largest_number}")
print(f"this is the smallest element: {smallest_number}")

