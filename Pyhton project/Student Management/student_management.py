class StudentDatabase:
    def __init__(self) -> None:
        self.student_list = []
        # return self.student_list //  __init__ eta kono value return korte pare na

    def add_student(self, student):
        self.student_list.append(student)
        # return self.student_list
    
class Student:
    def __init__(self, student_id, name, department, is_enrolled) -> None:
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if self.is_enrolled == True:
            print('Student is already enrolled')
        else:
            self.is_enrolled = True
            print('Student enrolled successfully')

    def drop_student(self):
        if self.is_enrolled:
            self.is_enrolled = False
            print('Student dropped successfully')
        else:
            print('Student is not enrolled')

    
robin = Student(223301, 'Robin', 'CSE', True)
kobir = Student(223302, 'Kobir', 'CSE', True)
chobir = Student(223303, 'Chobir', 'CSE', True)
mofij = Student(223304, 'mofij', 'CSE', False)
hasem = Student(223305, 'hasem', 'CSE', True)

student = [robin, kobir, chobir, mofij, hasem]
database = StudentDatabase()

for st in student:
    database.add_student(st)

# database.add_student(chobir) 
# database.add_student(kobir) 

for st_list in database.student_list:
    print(st_list.name)
    # print(st_list.student_id)


print('\n')

mofij.enroll_student()

hasem.enroll_student()
print(hasem.is_enrolled)

hasem.drop_student()
print(hasem.is_enrolled)