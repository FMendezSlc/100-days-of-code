from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    q_text = entry['text']
    q_answer = entry['answer']

    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

print(f"You've finished the quiz!!\nYour final score is: {quiz.score}/{quiz.question_number}")