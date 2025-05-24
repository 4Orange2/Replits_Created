# This program aims to find a given word in a matrix of letters
# The letters don't need to be put together in a given line segment
  # You take one letter and then you look at the nine spaces around it
  # If the second letter is present, then continue in that direction (use the same recursive idea for keeping track of all the occurences of the first letter, then all the occurences of the second leter, then all the occurences of third letter)
  # Note: you can't use the same letter once

amnt_of_rows = int(input("How many rows? ")) 
amnt_of_columns = int(input("How many columns? "))

matrix = [['N', 'A', 'T', 'S', 'F', 'E', 'G', 'Q', 'N'], ['S', 'A', 'I', 'B', 'M', 'R', 'H', 'F', 'A'], ['C', 'F', 'T', 'J', 'C', 'U', 'C', 'L', 'T'], ['K', 'B', 'H', 'U', 'P', 'T', 'A', 'N', 'U'], ['D', 'P', 'R', 'R', 'R', 'J', 'D', 'I', 'R'], ['I', 'E', 'E', 'K', 'M', 'E', 'G', 'B', 'E']]

word_is_present = 0 # the end value of the program
'''
for i in range(amnt_of_rows):
  row_characters = (input(f"List your {amnt_of_columns} characters for the row: ")).split(" ")
  matrix.append(row_characters)
'''
print(matrix)

word = input("What is the word you want the program to find? ")


def eligible(row_and_column, coming_from_coordinate, bend_status):
  '''Determines whether a given coordinate is eligible to be searched.
  Returns a list called "coordinates_to_search"'''
  # should be correct
  initial_row = row_and_column[0]
  print(f"this is our {initial_row}")
  initial_column = row_and_column[1]
  print(f"this is our {initial_column}")
  row_range = [initial_row-1, initial_row+1] # all three of the possible rows that can be explored
  col_range = [initial_column-1, initial_column+1] # all three of the possible columns that can be explored

  coordinates_to_search = []
  if coming_from_coordinate == None: # this determines the spaces to be searched for the second letter
    #correct
    if initial_row == 0: # you need to make sure to change from if's to elif's
      row_range[0] = initial_row
    if initial_column == 0:
      col_range[0] = initial_column
    if initial_row == (amnt_of_rows - 1):
      row_range[1] = initial_row
    if initial_column == (amnt_of_columns - 1):
      col_range[1] = initial_column
    print(f"this is row_range {row_range}")
    print(f"this is col_range {col_range}")
    for row in range(row_range[0], row_range[1] + 1):
      for col in range(col_range[0], col_range[1] + 1):
        if col == initial_column and row == initial_row:
          pass
        else:
          coordinates_to_search.append([row, col])
  elif coming_from_coordinate != None: 
    # this determines the spaces after a general direction has been determined, there can only be one bend in the search from now on 
    row_diff = initial_row - coming_from_coordinate[0] # the answer will either +1, -1, or 0
    print(f"this is our row_diff {row_diff}")
    col_diff = initial_column - coming_from_coordinate[1] # the answer will either be +1, -1, or 0
    print(f"this is our col_diff {col_diff}")
    if (initial_row + row_diff) < 0 or (initial_row + row_diff) >= amnt_of_rows or (
      initial_column + col_diff) < 0 or (initial_column + col_diff) >= amnt_of_columns: # this "if" looks to see if there are possiblities for indexes out of range if we continue in the same direction 
      pass
    else:
      coordinates_to_search.append([initial_row + row_diff, initial_column + col_diff])
    if bend_status == True: # meaning that there hasn't been a bend in the pathway yet
      if row_diff != 0 and col_diff != 0: # i.e. it's diagonal
        print("our bend is diagonal")
        if (initial_row - row_diff) >= 0 and (initial_row - row_diff) < amnt_of_rows and (
          initial_column + col_diff) >= 0 and (initial_column + col_diff) < amnt_of_columns: # for a bend to the left of your current direction
          coordinates_to_search.append([initial_row - row_diff, initial_column + col_diff, "bended"])
        if (initial_row + row_diff) >= 0 and (initial_row + row_diff) < amnt_of_rows and (
          initial_column - col_diff) >= 0 and (initial_column - col_diff) < amnt_of_columns: # for a bend to the right of your current direction
          coordinates_to_search.append([initial_row + row_diff, initial_column - col_diff, "bended"])
      else: # it's horizontal or vertical
        print("our bend is horizontal or vertical")
        if row_diff == 0: # if we've been going horizontally up until now
          print("we've been going horizontally")
          if (initial_row - col_diff) >= 0 and (initial_row - col_diff) < amnt_of_rows: # because col_diff is zero, it doesn't need to be considered
            print("-row_diff")
            coordinates_to_search.append([initial_row - col_diff, initial_column, "bended"])
          if (initial_row + row_diff) >= 0 and (initial_row + row_diff) < amnt_of_rows:
            print("+row_diff")
            coordinates_to_search.append([initial_row + col_diff, initial_column, "bended"])
        elif col_diff == 0: # because row_diff is zero, it doesn't need to be considered
          print("we've been going vertically")
          if (initial_column - row_diff) >= 0 and (initial_column - row_diff) < amnt_of_columns:
            coordinates_to_search.append([initial_row, initial_column - row_diff, "bended"])
          if (initial_column + row_diff) >= 0 and (initial_column + row_diff) < amnt_of_columns:
            coordinates_to_search.append([initial_row, initial_column + row_diff, "bended"])
  print(f"this is our first coordinates_to_search: {coordinates_to_search}")
  return coordinates_to_search



def search_spaces(row_and_column, index_of_word, coming_from_coordinate, bend_status, word_is_present): # nothing is wrong in this fucntion
  '''Searches the spaces around the given row and column
  - after the first letter is identified, it searches the nine spaces around that first letter
  - after the second letter is picked, there is a direction determined, and now the nine spaces
  become limited to three spaces (because the word is allowed to have one perpendicular twist)
  - a list of the row and the column of the element that you want to search around'''
  desired_letter = word[index_of_word]
  print(f"this is {desired_letter}")
  last_index = len(word) - 1
  coordinates_to_search = eligible(row_and_column, coming_from_coordinate, bend_status)
  for coordinate in coordinates_to_search:
    print(f"this is the coordinate being considered: {coordinate}")
    if matrix[coordinate[0]][coordinate[1]] == desired_letter: # where coordinate[0] is the row and coordinate[1] is the column
      print("desired letter has been found")
      if index_of_word == last_index:
        word_is_present += 1 # after we get here, the function will start to drop back and start to test each previous for loop until we get to the initial for loop with all the possible spaces around the first occurences
        print("one has been added to word_is_present")
      else:
        if len(coordinate) == 3:
          if coordinate[2] == "bended":
            search_spaces(coordinate, index_of_word + 1, row_and_column, False, word_is_present)
        else:
          search_spaces(coordinate, index_of_word + 1, row_and_column, bend_status, word_is_present)

def occurences_of_first_letter(word, matrix, word_is_present): #correct
  '''a function to find the amount of times the first letter of our word is brought up in our matrix
  '''
  first_letter = word[0]
  first_letter_positions = []
  coordinate_row = 0
  coordinate_col = 0
  for row in matrix: # two simple nested for-loops to search through a matrix
    for character in row:
      if character == first_letter:
        first_letter_positions.append([coordinate_row, coordinate_col])
      coordinate_col += 1
    coordinate_col = 0
    coordinate_row += 1
  print(first_letter_positions)
  for first_letter_coordinate in first_letter_positions: # we search for a second letter beside every first_letter_coordinate
    search_spaces(first_letter_coordinate, 1, None, True, word_is_present)

  return word_is_present


occurences_of_word = occurences_of_first_letter(word, matrix, word_is_present)
print(f"these are how many occurences that I found of the word: {occurences_of_word}")