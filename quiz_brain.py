class QuizBrain:

    def __init__(self, list):
        self.q_number = 0
        self.q_list = list
        self.q_answer = None
        self.score = 0

    def still_has_questions(self):
        return len(self.q_list) > self.q_number

    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        self.q_answer = question.answer
        return f"Q.{self.q_number}: {question.text}"

    def check_answer(self, user_answer):
        if user_answer.lower() == self.q_answer.lower():
            self.score += 1
            return True
        else:
            return False
