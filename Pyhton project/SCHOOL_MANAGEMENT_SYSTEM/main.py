from school import School
from person import Teacher, Student
from classroom import ClassRoom
from subject import Subject

school = School("ABC", "Dhaka")

# Adding Classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Tem")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding Student
robin = Student("Robin", eight)
jibon = Student("Jibon", nine)
shobin = Student("Shobin", ten)
roton = Student("Roton", ten)

school.student_admission(robin)
school.student_admission(jibon)
school.student_admission(shobin)
school.student_admission(roton)


# Adding Teacher
motiur = Teacher("Motiur Rahama")
habib = Teacher("Rowshon Habib")
azad = Teacher("Abdullah Al Azad")
riyajul = Teacher("Riyajul Islam")


# Adding Subject
chemistry = Subject("Chemistry", motiur)
biology = Subject("English", habib)
sports = Subject("Sports", azad)
english = Subject("English", riyajul)

eight.add_subject(english)
eight.add_subject(chemistry)
eight.add_subject(sports)

nine.add_subject(biology)
nine.add_subject(chemistry)
eight.add_subject(english)

ten.add_subject(english)
ten.add_subject(chemistry)
ten.add_subject(biology)
ten.add_subject(sports)

eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()

print(school)