highest_int = int(input("Enter an integer: "))

string_to_print = ""

for i in range(1,highest_int + 1):
  if (i % 3) == 0 and (i % 5) == 0:
    string_to_print += "FizzBuzz "
  elif (i % 3) == 0:
    string_to_print += "Fizz "
  elif (i % 5) == 0:
    string_to_print += "Buzz "
  else:
    string_to_print += f"{i} "

print(string_to_print)