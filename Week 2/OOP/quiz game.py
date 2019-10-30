class Question:
    def __init__(self, questions, answers):
        self.__questions = questions
        self.__answers = answers

    def get_question(self):
        return self.__questions

    def is_answer_correct(self, answer):
        if self.__answers == answer:
            return 1
        else:
            return 0

class Quiz:

