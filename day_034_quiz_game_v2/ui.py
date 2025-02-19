from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
COLOR_RED = "red"
COLOR_GREEN ="green"
class QuizInterface:



    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer app")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = Label(text="score: 0", highlightthickness=0,
                                 bg=THEME_COLOR,font=("Arial", 10, "italic"),fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        question = "Some Question"
        self.question_text = self.canvas.create_text(150, 125, text=question, width=250, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_click)
        self.true_button.grid(row=2, column=0, padx =20, pady =20)
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_click)
        self.false_button.grid(row=2, column=1, padx =20, pady =20)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            question =self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="Thank You for participating,"
                                                            " you have answered all questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.give_feedback( self.quiz.check_answer(True))

    def false_click(self):
        self.give_feedback( self.quiz.check_answer(False))

    def give_feedback(self,answer):
        if answer:
            self.canvas.config(bg=COLOR_GREEN)
        else:
            self.canvas.config(bg=COLOR_RED)
        self.window.after(500,self.get_next_question)




