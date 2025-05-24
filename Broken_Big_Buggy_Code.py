# Program that finds the smallest number among the three input numbers
# It then tells you if it is negative, positive.
# If it is 0, it asks you a math problem.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 <= num2) and (num1 <= num3):
  smallest = num1
  
elif (num2 <= num1) and (num2 <= num3):
  smallest = num2

else:
  smallest = num3
  
print(f"The smallest number is {smallest}")

if smallest >= 0:
  
  if smallest == 0:
    answer = int(input(f"You win a math question! What is {num1} plus {num2}? "))
    
    if answer == (num1 + num2):
      print("Correct!")
    else:
      print("Wrong!")

  else:
    print("That is a positive number")

else:
  print("That is a negative number")