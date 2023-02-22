import quiz_brain
from tkinter import *

FONT = ("Arial", 20, "italic")
COLOR = "#375362"
TICK_MARK = "images/true.png"
CROSS_MARK = "images/false.png"


class UI:

    def __init__(self, quiz_brain: quiz_brain.QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=COLOR)

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=COLOR,
            font=("Arail", 14, "normal"),
        )
        self.score_label.grid(column=1, row=0, sticky="e")

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0,
        )
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=COLOR,
            font=FONT,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        tick_img = PhotoImage(file=TICK_MARK)
        self.true_button = Button(
            image=tick_img,
            bg=COLOR,
            bd=0,
            activebackground=COLOR,
            command=self.true_pressed,
        )
        self.true_button.grid(column=0, row=2)

        cross_img = PhotoImage(file=CROSS_MARK)
        self.false_button = Button(
            image=cross_img,
            bg=COLOR,
            bd=0,
            activebackground=COLOR,
            command=self.false_pressed,
        )
        self.false_button.grid(column=1, row=2)

        self.display_next_question()
        self.window.mainloop()

    def display_next_question(self):
        question = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.text, text=question)

    def true_pressed(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.display_result(self.quiz_brain.check_answer("True"))

    def false_pressed(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.display_result(self.quiz_brain.check_answer("False"))

    def display_result(self, user_guess):
        if user_guess:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.config(bg="red")
        self.canvas.itemconfig(self.text, fill="white")
        self.window.after(1000, self.move_on)

    def move_on(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.text, fill=COLOR)
            self.true_button.config(state="active")
            self.false_button.config(state="active")
            self.display_next_question()
        else:
            self.end_game()

    def end_game(self):
        self.canvas.config(bg=COLOR)
        self.canvas.itemconfig(
            self.text,
            text=f"The Quiz is over.\nFinal Score: {self.quiz_brain.score}",
        )

        self.score_label.config(text="")
