grade = int(input("What is your grade level? "))

if grade >= 1 and grade <= 6:
  statement = "Elementary School"
elif grade >= 7 and grade <= 8:
  statement = "Middle School"
elif grade >= 9 and grade <= 12:
  statement = "High School"
else:
  statement = "I don't know what grade is"

print(f"{statement}")
  