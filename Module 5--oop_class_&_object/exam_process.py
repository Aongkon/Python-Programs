class Exam:
    def __init__(self, name):
        self.name = name
        self.attendance = 'attend'
        self.min_marks = 40
        self.max_marks = 80
    def attend_for_exam(self, attend):
        if self.attendance != attend:
            print('the student is not here')
        else:
            print('the student is here. he need to retake exam.')
    def get_marks(self, marks):
        if marks < self.min_marks:
            print(f'you get {marks} mark and you are fail in the exam.')
        elif marks >= self.min_marks and marks < self.max_marks:
            print(f'you get {marks} mark and you pass in this exam')
        else:
            print(f'you get {marks} mark and your marks is best')

aongkon = Exam('aongkon')
aongkon.attend_for_exam('attend')
aongkon.get_marks(50)

kongkon = Exam('kongkon')
kongkon.attend_for_exam('not here')
# kongkon.get_marks(33)