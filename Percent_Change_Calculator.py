First_num = int(input(""))
Second_num = int(input(""))

if First_num < Second_num:
  decrease = First_num/Second_num * 100
  print(f"{decrease} % decrease")
elif First_num > Second_num:
  increase = First_num/Second_num * 100
  print(f"{increase} % increase")
elif First_num == Second_num:
  print("No increase or decrease")