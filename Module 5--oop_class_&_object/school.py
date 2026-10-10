class Students:
    def __init__(self, name, current_cls, id):
        self.name = name
        self.current_cls = current_cls
        self.id = id
    def __str__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_cls}, id: {self.id}'
class Teachers:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'teacher: {self.name}, subject: {self.subject}, id:{self.id}'
class School:
    def __init__(self, scl_name):
        self.scl_name = scl_name
        self.teachers = []
        self.students = []
        
    def add_teachers(self, name, subject):
        id = len(self.teachers) + 1
        faculty = Teachers(name, subject, id) # object for class
        self.teachers.append(faculty)

    def enroll(self, name, fee):
        if fee < 6500:
            return f'Not enough fee'
        else:
            id = len(self.students) + 1
            pupil = Students(name, 'C', id)
            self.students.append(pupil)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('Welcome to', self.scl_name)
        print('---------OUR TEACHERS---------')
        for teacher in self.teachers:
            print(teacher)
        print('---------OUR STUDENTS---------')
        for student in self.students:
            print(student)
        return 'All done for now'


phitron = School('Phitron')


phitron.enroll('Mithila', 11100)
phitron.enroll('Mithila', 80000)
phitron.enroll('Sunny', 90000)
phitron.enroll('Aongkon', 5200)

phitron.add_teachers('Piash', 'DS')
phitron.add_teachers('Moti', 'Algo')
phitron.add_teachers('Azad', 'C++')



print(phitron)
