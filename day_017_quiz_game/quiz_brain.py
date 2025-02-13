class QuizBrain():
    def __init__(self, question_bank):
        self.question_number = 0
        self.points = 0
        self.question_bank = question_bank

    def ask_question(self):
        self.question_number += 1
        question =  self.question_bank[self.question_number -1]
        answer = input(f"{self.question_number}: {question.text} (True/False): ")
        if answer == question.answer:
            print("You answered correctly")
            self.points +=1
            self.calculate_points()
        else:
            print("You answered incorrectly")
            print(f"Correct answer: {question.answer} ")
            self.calculate_points()

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)


    def calculate_points(self):
        print(f"You have {self.points}/{self.question_number} points \n")