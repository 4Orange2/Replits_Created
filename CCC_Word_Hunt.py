# an if statement for words that are spelt backwards

# occurences_of_word = 0

# identify first letter by searching through whole grid
# if no letter, then terminate
# elif letter (for however many there are)
  # search the nine spaces around the letter
  # If the second letter of the word is present:
    # for however many times the second letter is present:
      # search for the third letter in the direction of the second letter (remember, it could be perpendicular - so you need to check four locations)
      # search for the third letter - always keep the perpendicular option open
    # keep on going until the end of the word is reached - if you take the perpendicular path, then you can't take another perpendicular turn; you're done and you continue straight
    # once this process is done, either add 1 to occurences_of_word or don't add anything and move on to the next letter in the list
