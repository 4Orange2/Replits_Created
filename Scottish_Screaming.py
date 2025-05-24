vowels = ['a','e','i','o','u','y']

initial = str(input("What is the sentence that you want to enter? "))

for i in range(len(initial)):
  character = initial[i]
  if not character.isalpha():
    pass
  else:
    for vowel in vowels:
      if character == vowel:
        initial = initial.replace(character,"e")        
        break
  
print(initial)