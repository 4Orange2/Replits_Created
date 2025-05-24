# no negative number

number = int(input("Your number: "))

amnt_of_sevens = number // 7
amnt_of_fours = (number - (amnt_of_sevens * 7)) // 4 
amnt_of_ones = (number - (amnt_of_sevens * 7) - (amnt_of_fours * 4)) // 1

if amnt_of_sevens == amnt_of_fours  == amnt_of_ones:
  print(f"{amnt_of_sevens} 7s, {amnt_of_fours} 4s, {amnt_of_ones} 1s")
  print("Equal number of 1s, 4s, and 7s!")
else:
  print(f"{amnt_of_sevens} 7s, {amnt_of_fours} 4s, {amnt_of_ones} 1s")
