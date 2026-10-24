import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    # def teach(self, name, age, sub, add, cls):
    #     self.name = name
    #     self.age = age
    #     self.sub = sub
    #     self.add = add
    #     self.cls = cls
    def evaluate_exam(self):
        random.randint(1, 100)

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}  # {"ict" : 34, }
        self.subject_grade = {}  # {"eng" : "A", }
        self.grade = None

    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.value():
            point = School.grade_to_value(grade)
            sum += point
        gpa = sum / len(self.subject_grade)
        self.grade = School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id 
    @id.setattr
    def id(self, value):
        self.__id = value


        