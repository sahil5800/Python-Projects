from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dic in question_data:
    question_text=dic["text"]
    question_answer=dic["answer"]
    question=Question(question_text, question_answer )
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions()==True:
    quiz.next_question()

print("\n\n\n\n\n\ntrYou have completed the quiz")
print(f"your final score was: {quiz.score}/{len(question_bank)}")