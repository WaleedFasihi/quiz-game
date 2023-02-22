import ui
import data
import html
import quiz_brain
import question_model

question_bank = []

for question in data.question_data:
    text = html.unescape(question["question"])
    answer = question["correct_answer"]
    question_bank.append(question_model.Question(text, answer))

quiz = quiz_brain.QuizBrain(question_bank)
quiz_ui = ui.UI(quiz)
