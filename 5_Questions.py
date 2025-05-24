#FIVE QUIZ QUESTIONS  (Make up your own questions :) )
q1 = "What is Mr. Seger's favourite video game? "
q2 = "Which famous irrational number starts with the digits 2.71828...? "
q3 = "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a...? "
# I know these questions don't actually have correct answers; but you know, for fun. 
q4 = "What is the best sport in the world? "
q5 = "what is the best season? " 

question_list = [q1, q2, q3, q4, q5]

#THE FIVE CORRECT ANSWERS
a1 = "Rocket League"
a2 = "e"
a3 = "duck"
a4 = "Soccer" #make 2 more
a5 = "Summer"



#MAKING AN ARRAY OUT OF THE CORRECT ANSWERS
correctAnswers = [a1, a2, a3, a4, a5]


#THE USER TAKES THE QUIZ.  STORE THEIR RESPONSES IN THE ARRAY userGuesses
userGuesses = []

for question in question_list:
    user_answer = input(question) 
    userGuesses.append(user_answer)
    

#THE PROGRAM MARKS THE QUIZ AND TELLS THE USER WHICH ONES THEY GOT RIGHT
score = 0

for i in range(len(userGuesses)):
    if userGuesses[i] == correctAnswers[i]:
      score += 1

print(f"Your final score is: {score}")