#Make an Quiz which takes various questions from a file, picked randomly.

'''Antonyms Based Quiz'''
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
question_prompts = [
     "What does 'superficial' antonym?\n(1) 'deep'\n(2)'shallow'",'\n'
     "What does 'juvenile' antonym?\n(1) 'control'\n(2)'mature'",'\n'
    "What does 'gratuity' antonym?\n (1) 'wages'\n (2) 'discount'", '\n'
    "What does 'sanguine' antonym?\n (1) 'bloodless'\n (2) 'serious'", '\n'
    "What does 'bliss' antonym?\n (1) 'rapture'\n (2) 'misery'", '\n'
]
name = input("Please enter your name: ").title()
questions = [
     Question(question_prompts[0], "1"),
     Question(question_prompts[1], "2"),
    Question(question_prompts[2], "1"),
    Question(question_prompts[3], "1"),
    Question(question_prompts[4], "2")
              ]
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("\n{0}, you scored {1} out of {2}.".format(name, score, len(questions)))
run_quiz(questions)