from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
questionBank = []
for question in question_data:
    question_txt = question["text"]
    question_ans = question["answer"]
    new_ques = Question(question_txt, question_ans)
    questionBank.append(new_ques)

quiz = QuizBrain(questionBank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"your final score is {quiz.score}/{len(questionBank)}")