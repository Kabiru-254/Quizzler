from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15))
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        self.question_os = self.canvas.create_text(150, 125, width=280, font=("Arial", 15),
                                                   fill=THEME_COLOR)

        true_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=true_image, highlightthickness=0, cursor="heart", command=self.is_true)
        self.right_button.grid(row=3, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, cursor="heart", command=self.is_false)
        self.wrong_button.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.change_background("white")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_os, text=question_text)
        else:
            self.change_background("white")
            self.canvas.itemconfig(self.question_os, text=f"Test over! you scored {self.quiz.score} out of 10!")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.change_background("green")
        else:
            self.change_background("red")
        self.window.after(1000, self.get_next_question)

    def change_background(self, color: str):
        self.canvas.config(bg=color)
