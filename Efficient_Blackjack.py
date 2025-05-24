import random
player_hand = int(random.randint(1, 10) + random.randint(1, 10))
exit = False
while exit == False:
  print(f"Your hand is {player_hand}")
  if player_hand == 21:
    print("the player wins")
  if player_hand > 21:
    print("the dealer wins")
  pass_or_draw = input("Do you wish to 'pass' or 'draw'? ")
  if pass_or_draw == "pass":
    dealer_hand = random.randint(2,21)
    print(f"this is the dealer's hand {dealer_hand}")
    exit = True
  elif pass_or_draw == "draw":
    player_hand += int(random.randint(1, 10))
result = "draw" if dealer_hand == player_hand else (
  "the dealer wins" if dealer_hand > player_hand else "the player wins")
print(result)