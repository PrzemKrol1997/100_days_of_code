from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]
for create_new_question in range(0, len(question_data)):
    question_bank.append(Question(question_data[create_new_question]["question"],(question_data[create_new_question]["correct_answer"])))
    #print(question_bank[create_new_question].text,question_bank[create_new_question].answer )
quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.ask_question()

print(f"You have completed quiz, your final score is {quiz.points}/{quiz.question_number}")