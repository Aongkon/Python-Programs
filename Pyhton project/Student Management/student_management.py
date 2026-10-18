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

    def view_student_info(self): # self parameter receive the object value
        # if view_st_id == self.student_id:
        print(f"Student ID: {self.student_id} \nName: {self.name} \nDepartment: {self.department} \nEnrollment Status: {self.is_enrolled}")
        
    def id_selector(self):
        print(f'{self.student_id}')

    
robin = Student(223301, 'Robin', 'CSE', False)
kobir = Student(223302, 'Kobir', 'CSE', False)
chobir = Student(223303, 'Chobir', 'CSE', False)
mofij = Student(223304, 'mofij', 'CSE', True)
hasem = Student(223305, 'hasem', 'CSE', False)

student = [robin, kobir, chobir, mofij, hasem]
database = StudentDatabase()

for st in student:
    database.add_student(st)

for idx, st_info in enumerate(student):
    print(idx)
    print('----')
    Student.view_student_info(st_info)
    print('\n')

for idx, st in enumerate(student):
    Student.id_selector(st)


# database.add_student(chobir) 
# database.add_student(kobir) 

# for st_list in database.student_list:
#     print(st_list.name)
    # print(st_list.student_id)


# print('\n')

# mofij.enroll_student()

# hasem.enroll_student()
# print(hasem.is_enrolled)

# hasem.drop_student()
# print(hasem.is_enrolled)


while True:
    print("\n============= Student Management System =================")
    print("1. View all Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input('Enter your choice: ')
    if choice == '1':
        for st in database.student_list:
            print('------------------------')
            # print(Student.view_student_info(st))  method nijey call kortase tai alada vhabe st dewa lage na
            # print(Student.view_student_info())
            st.view_student_info()
    elif choice == '2':
        student_id = int(input('Enter the student ID: '))

        found_student = None
        for st in database.student_list:
            if student_id == st.student_id:
                # Student.enroll_student() 
                found_student = st
                break

        if found_student is not None:
            found_student.enroll_student()
        else:
            print('Error: Invalid Student ID.')

    elif choice == '3':
        student_id = int(input('Enter the student ID: '))
        found_student = None

        for st in database.student_list:
            if student_id == st.student_id:
                found_student = st
                break

        if found_student is not None:
            # Student.drop_student()
            found_student.drop_student()
        else:
            print("Error: Invalid Student ID.")

    elif choice == '4':
        print('Exiting Student Management System...')
        break

    else:
        print("Invalid choice. Please try again.")
