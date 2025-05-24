# Aims to find the first and second third places out of the "raceTimes"
raceTimes = [453, 450, 420, 492, 509, 444, 460, 530, 499]


for i in range(3):
  largest_number = 0
  for time in raceTimes:
    if time > largest_number:
      largest_number = time
  if i == 0:
    print(f"1st place: {largest_number}")
  elif i == 1:
    print(f"2nd place: {largest_number}")
  elif i == 2:
    print(f"3rd place: {largest_number}")
  raceTimes.remove(largest_number)
  
