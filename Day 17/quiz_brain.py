class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list


    def still_has_questions(self):
        return self.question_number != len(self.questions_list)

    def check_answer(self, answer, correct_answer):
        string = ""
        if answer == correct_answer.lower():
            self.score += 1
            string = "right"
        else:
            string = "wrong"
        print(f"You got it {string}!\nYour current score is: {self.score}/{self.question_number + 1}\n")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ").lower()

        self.check_answer(answer, current_question.answer)
        self.question_number += 1
