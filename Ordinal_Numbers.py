'''
#Test cases:
1
2
3
4
5
11
12
13
14
21
22
23
24
3411
693483
'''

while True:
    n = str(input("Any number: "))
    last_digit = int(n[-1])
  
    if last_digit < 4 and last_digit > 0:
      second_last_digit = int(n[-2])
      if second_last_digit == 1:  
        suffix = "th"
      else:
        if last_digit == 1:
          suffix = "st"
        elif last_digit == 2:
          suffix = "nd"
        elif last_digit == 3:
          suffix = "rd"
    else:
        suffix = "th"
    print(f"{n}{suffix}")
