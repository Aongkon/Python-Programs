class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # {"bangla": "roton bisshas"}
        self.classrooms = {} # {"eigHt": "jamil"}
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom 
    def add_teachers(self, subject, teacher):
        self.teachers[subject] = teacher
        