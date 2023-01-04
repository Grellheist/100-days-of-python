class QuizBrain():
    
    def __init__(self, input):
        self.question_number = 0
        self.question_list = input

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = input(f"Q.{self.question_number}: "
                              f"{current_question.text} (True/False)?: ")
