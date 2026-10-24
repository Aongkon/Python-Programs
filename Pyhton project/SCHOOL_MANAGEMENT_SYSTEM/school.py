class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}  # {'Bangla' : "teacher object"}
        self.classrooms = {}  # {'eight' : "classroom object"}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, subject, teacher):  # value = teacher , key = subject
        self.teachers[subject] = teacher  # subject tomo key er moddhe teacher value ke rakhtasi
    def student_admission(self, student):
        pass

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return "A+"
        elif marks >= 70 and marks <= 79:
            return "A"
        elif marks >= 60 and marks <= 69:
            return "A-"
        elif marks >= 50 and marks <= 59:
            return "B"
        elif marks >= 50 and marks <= 59:
            return "C"
        elif marks >= 40 and marks <= 49:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            "A+" : 5.00,
            "A" : 4.00,
            "A-" : 3.50,
            "B" : 3.00,
            "C" : 2.50,
            "D" : 2.00,
            "F" : 0.00
        }
        return grade_map[grade]
