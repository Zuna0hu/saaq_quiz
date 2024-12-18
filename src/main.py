from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# to construct a question bank

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

# print(question_bank)

Quiz = QuizBrain(question_bank)

while (Quiz.still_has_questions()):
    Quiz.next_question()
Quiz.print_final_score()