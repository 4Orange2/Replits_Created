# Problem 1: 
for table_number in range(1,11):
  print(f"\n Moving to place {table_number} \n Setting the plate \n Setting the fork and knife \n Filling the glass \n")

# Prolem 2: age that you're becoming in that year starting from 2020

age = 12

for i in range(81):
  if i < 10:
    print(f"202{i} {age + i}")
  elif i == 80:
    print(f"2100 {age + i}")
  else:
    print(f"20{20+i} {age + i}")

# Problem 3: Multiples of 5; starting from 20 and going all the way up to 100

for i in range(20,101,5):
  print(i)

# Problem 4: Printing after each addition for numbers 1 to 20

total = 0

for number in range(1,21):
  total += number
  print(f"the sum is {total}")

# Problem 5: Mark Entering

amount_of_marks = int(input("How many marks do you want to enter? "))

marks_list = []

for i in range(amount_of_marks):
  mark = int(input("Enter your percentage mark: "))
  marks_list.append(mark)
  if i == 0:
    print(f"you have entered {i+1} mark")
  else:
    print(f"you have entered {i+1} marks") 

average = sum(marks_list)/amount_of_marks
print(f"This is the average of your {amount_of_marks} grades: {average}")

