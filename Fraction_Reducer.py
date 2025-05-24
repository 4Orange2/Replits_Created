'''This program reduces a fraction by finding its gcd using the Euclidean Algorithm and accounts for the following special cases:
1. 0 as the denominator
2. 0 as the numerator
3. Negative numbers
4. GCD = 1
5. Denominator = 1
'''

print("Welcome to my fraction reducer!")

while True: # Ask
  numerator = int(input(("Enter the numerator: ")))
  denominator = int(input("Enter the denominator: "))
  
  if denominator == 0:
    print("This fraction is undefined")
  
  else:
    if numerator == 0:
      print(f"{numerator}/{denominator} = 0")
    
    else:
      if numerator < 0 or denominator < 0:
        print("Sorry, this program only handles non-negative numerators.")
      else:
        # Euclid's Algorithm:
        
        Max = max(numerator, denominator)
        Min = min(numerator, denominator)
        Remainder = Max % Min
        
        while Remainder != 0:
          Max = Min
          Min = Remainder
          Remainder = Max % Min
        
        new_numerator = int(numerator/Min)
        new_denominator = int(denominator/Min)
        
        if Min == 1 and new_denominator != 1:
          final_string = f"{numerator}/{denominator} is in already reduced form"
        else:
          if new_denominator == 1:
            final_string = f"{numerator}/{denominator} = {new_numerator}"
          
          else:
            final_string = f"{numerator}/{denominator} = {new_numerator}/{new_denominator}"
            
        print(final_string)