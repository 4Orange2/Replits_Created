Num1 = int(input("Number 1: "))
Num2 = int(input("Number 2: "))
Num3 = int(input("Number 3: "))
Operation1 = input('Type "multiply" or "divide": ')
Operation2 = input('Type "add" or "subtract": ')

answer = 0

if Operation1 == "multiply":
  if Operation2 == "add":
    answer = Num1 * Num2 - Num3
  elif Operation2 == "subtract":
    answer = Num1 * Num2 - Num3

elif Operation1 == "divide":
  if Operation2 == "add":
    answer = Num1 / Num2 + Num3
  elif Operation2 == "subtract":
    answer = Num1 / Num2 - Num3

print(f"try to figure out what I did with these numbers if this is the answer: {answer}")
  