import random

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # {"bangla": "roton bisshas"}
        self.classrooms = {} # {"eigHt": "jamil"}
    def add_classroom(self, classroom):  
        self.classrooms[classroom.name] = classroom  # classroom eta ekta object and etar moddhe std or sub ache

    def add_teachers(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        classname = student.classroom # classroom ta ashole student class er attribute 
        # abar ey classroom tai moloto ekta class jar moddhe students, subjects egolo ache
        classname.add_student(student)

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
    
    @staticmethod
    def value_to_grade(value):
        if value >= 5.00:
            return "A+"
        elif value >= 4.00 and value < 5.00:
            return "A"
        elif value >= 3.50 and value < 4.00:
            return "A-"
        elif value >= 3.00 and value < 3.50:
            return "B"
        elif value >= 2.50 and value < 3.00:
            return "C"
        elif value >= 2.00 and value < 2.50:
            return "D"
        else:
            return "F"
        
    def __repr__(self):
        # All class room
        for key in self.classrooms.keys():
            print(key)
        # All student
        print("All Student")


class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        pass
    def get_top_students(self):
        pass

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 40
    def exam(self, students):
        pass


class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def teach(self):
        pass
    def evaluate_exam(self):
        return random.randint(1, 100)

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.marks = {} # {"english": 67, 'bangla': 89}
        self.subject_grade = {} # {"ict" : "A"}
        self.total_grade = None 

    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point
            if sum == 0:
                gpa = 0.00
                grade = "F"
            else:
                gpa = sum / len(self.subject_grade)
                self.total_grade = School.value_to_grade(gpa)
            print(f'{self.name} final grade is: {self.total_grade}, with gpa: {gpa}')



    @property
    def id(self):   # getter ekhan theke id return paro
        return self.__id
    
    @id.setter  # eta set kortase
    def id(self, value):
        self.__id = value


#############

school = School("CHS", "Cawrasta")

# adding classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding student
robi = Student("Robi", nine)  # classroom er object amara ekhane dhokaia ditasi bro
shomi = Student("Shomi", eight)
hasib = Student("Hasib", ten)
jahid = Student("Jahid", nine)

# student admission
school.student_admission(robi)
school.student_admission(shomi)
school.student_admission(hasib)
school.student_admission(jahid)


# adding teacher 
riajul = Teacher("Riajul")
motiur = Teacher("Motiur")
habib = Teacher("Habib")

# adding subject
english = Subject("English", riajul)
chemistry = Subject("Chemistry", motiur)
biology = Subject("Biology", habib)







# school.add_classroom("Eight")
# school.add_classroom("Nine")
# school.add_classroom("Ten")


# school.add_teachers("English", "Riyajul")
# school.add_teachers("Chemistry", "Motiur")
# school.add_teachers("Biology", "Habib")

# robi.classroom