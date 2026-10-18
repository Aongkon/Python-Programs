class StudentDatabase:
    def __init__(self) -> None:
        self.student_list = []
        # return self.student_list //  __init__ eta kono value return korte pare na

    def add_student(self, student):
        self.student_list.append(student)
        # return self.student_list
    
class Student:
    def __init__(self, student_id, name, department, is_enrolled) -> None:
        self._student_id = student_id
        self._name = name
        self._department = department
        self.is_enrolled = is_enrolled

    
robin = Student(223301, 'Robin', 'CSE', True)
kobir = Student(223302, 'Kobir', 'CSE', True)
chobir = Student(223303, 'Chobir', 'CSE', True)
mofij = Student(223304, 'mofij', 'CSE', True)
hasem = Student(223305, 'hasem', 'CSE', True)

student = [robin, kobir, chobir, mofij, hasem]
database = StudentDatabase()

for st in student:
    database.add_student(st)

# database.add_student(chobir) 
# database.add_student(kobir) 

for st_list in database.student_list:
    print(st_list._name)
    # print(st_list._student_id)