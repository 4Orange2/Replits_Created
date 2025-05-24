#THIS GAME LETS THE USER PLAY A DICE ROLLING GAME UNTIL THEY GOES BUST, WINS OVER $1000 OR QUITS

# hack identified: if you enter a negative number for the bet (because obviously losing your bet is much more likely) if you subtract a negative number, you get a positive number 
# 

from random import *

#PRINT THE INSTRUCTIONS
print("This is a dice-rolling game.  You have $100 to start.")
print("Your goal is to reach $1000 before you go bust, but you can quit and keep your winnings at any time.")
print("Place a bet before you roll.")
print("If you roll a total of 7 or 11, you win double your bet.")
print("If you roll double, you break even.")
print("Otherwise, you lose your bet." + "\n")
print()

balance = 100
playAgain = "yes"


#GAME LOOP. THIS REPEATS FOR AS LONG AS THE USER'S BALANCE IS BETWEEN $0 AND $1000 AND THE USER WANTS TO KEEP PLAYING
# in[] function stands for the range of values that can work for a given condition

while playAgain in ["yes", "YES", "Yes", "y", "Y", "sure"]:
  bet = int(input("Enter your bet (non-negative integer): $"))
  while bet < 0:
    print("not an acceptable input")
    bet = int(input("Enter your bet (non-negative integer): $"))
  die1 = randint(1,6)   #GET TWO RANDOM DIE ROLLS. THE randint() COMMAND PICKS A RANDOM INTEGER BETWEEN TWO GIVEN VALUES, IN THIS CASE, 1 AND 6
  die2 = randint(1,6)

  dieTotal = die1 + die2

  print( "\n" + "You rolled a", die1, "and a", die2)

  if dieTotal == 7 or dieTotal == 11:   #PLAYER WINS DOUBLE WHAT THEY BET
    winAmount = 2*bet
    print( "You win $" + str(winAmount))
    balance = balance + winAmount
    if balance >= 1000:
      break

  elif die1 == die2:   #PLAYER BREAKS EVEN
    print( "You broke even; nothing happens" )

  else:   #PLAYER LOSES THEIR BET
    print( "You lose $" + str(bet) )
    balance = balance - bet
    if balance <= 0:
      break

  print("You now have $" + str(balance) + "\n")

  playAgain = input("Play again?") #ASK PLAYER IF THEY WANT TO KEEP PLAYING
    
#######
#THE LOOP IS NOW FINISHED. NOW WE USE AN IF-STATEMENT TO DETERMINE WHY THE LOOP STOPPED, AND GIVE AN APPROPRIATE RESPONSE
#######

if balance >= 1000:
  print("Congratulations! You have reached $1000!")

elif balance <= 0:          
  print("Sorry, you have gone bust.")

else: #THE USER QUIT
  print("Giving up so soon?!  Well, okay.  Your final balance is $" + str(balance))
