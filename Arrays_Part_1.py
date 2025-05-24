# exercise A

animals = ["cat", "dog", "lemur", "chimpanzee"]
for i in range(len(animals)):
  animals[i] = animals[i] + "s"

print(animals)

# exercise B

report_card_marks = [67, 47, 98, 40, 78, 0, 50, 53, 42, 50, 49, 88, 91, 6, 32, 50, 71, 95, 32, 70, 11, 85]

for i in range(len(report_card_marks)):
  mark = report_card_marks[i]
  if mark == 50:
    report_card_marks[i] = 51
  elif mark > 45 and mark < 50:
    report_card_marks[i] = 45
  elif mark > 0 and mark < 34:
    report_card_marks[i] = 35

print(report_card_marks)
