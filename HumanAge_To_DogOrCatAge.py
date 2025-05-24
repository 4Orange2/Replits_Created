'''I created a program based on the following requirements:
At least 1 input statement that asks for text (yes)
At least 1 input statement that asks for a number (yes)
At least 1 nested if-statement (if-statement within an if-statement) (yes)
At least 1 formula that computes something useful (yes)
At least 1 creative idea that makes your program fun or useful for others.  That is, your program should be something you enjoy writing. (yes)

The numbers for cat years used are based off of this link:
- https://natusan.co.uk/blogs/inside-scoop/how-do-cat-years-work-how-old-is-my-cat
The numbers used for dog years are based off of this link:
- https://www.pumpkin.care/blog/dog-age-chart/
'''

animal = input("Do you like 'cats' more or 'dogs'? ")
human_age = int(input("How old are you? "))

if animal == "cats": 
  if human_age == 1:
    years = human_age + 14
  elif human_age == 2:
    years = human_age + 13 + 9
  else: 
    years = human_age * 4 + 16
  print(f"{years} cat years old")
elif animal == "dogs":
  if human_age == 1:
    years = human_age + 14
  elif human_age == 2:
    years = human_age + 13 + 9
  else: 
    years = human_age * 5 + 16
  print(f"{years} dog years old")
else:
  print("This program doesn't work for those inputs")

