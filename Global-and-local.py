x = 100
y = 20


def doSomething(a):
  x = 5

  b  = y * a
  c = x*a
  
  print("The value of x in the function is", x)
  print("The value of y in the function is", y)
  print("The value of a in the function is", a)
  print("The value of b in the function is", b)



doSomething(2)

print("The value of x outside the function is", x)
print("The value of y outside the function is", y)
print("The value of a outside the function is", a)
print("The value of b outside the function is", b)