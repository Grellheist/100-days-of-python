import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_text = tk.Label(
                text="Score: 0",
                bg=THEME_COLOR,
                fg="white"
                )
        self.score_text.grid(column=1, row=0)
        correct_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(
                image=correct_image,
                highlightthickness=0,
                command=self.correct
                )
        self.true_button.grid(column=0, row=2)
        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(
                image=false_image,
                highlightthickness=0,
                command=self.false
                )
        self.false_button.grid(column=1, row=2)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
                150,
                125,
                width=280,
                text="Placeholder text",
                fill=THEME_COLOR,
                font=("Arial", 20, "italic")
                )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_text.config(
                    text=f"Score {self.quiz.score}"
                    )
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                    self.question_text,
                    text="You've reached the end of the quiz!"
                    )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
