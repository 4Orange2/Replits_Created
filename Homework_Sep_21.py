# Special cases to consider:
# b is negative
# m is 1 or -1
# b is 0
# m is 0
# undefined slope
  # x = 0

m = (input("Enter m: "))
if m == "undefined":
  x_int = int(input("What is the x-intercept? "))
  EOL = f"x = {x_int}"

else:
  b = int(input("Enter b: "))
  
  m = int(m)
  
  if b < 0:
    string_b = f"- {abs(b)}"
  elif b > 0:
    string_b = f"+ {abs(b)}"
  elif b == 0:
    string_b = "0"
  
  if abs(m) == 1:
    if m == -1:
      m = "-"
    elif m == 1:
      m = ""
    EOL = (f"y = {m}x {string_b}")
  elif m == 0:
    if b > 0:
      EOL = (f"y = {abs(b)}")
    elif int(b[-1]) <  0:
      EOL = (f"y = -{abs(b)}")
    elif int(b[-1]) == 0:
      EOL = ("y = x")
  else:
    EOL = f"y = {m}x {string_b}"

print(f"The EOL is {EOL}")