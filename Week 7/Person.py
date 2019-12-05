class Person:
    def __init__(self, email, firstname, lastname):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return self.firstname + ' ' + self.lastname

# Part (a) Create Instructor class, initializer and methods
class Instructor(Person):
    def __init__(self, email, firstname, lastname):
        self.students = {}
        super().__init__(email, firstname, lastname)

    def get_name(self):
        return f"{self.firstname} {self.lastname} (Instructor)"

    def add_student(self, student):
        self.students[student.email] = student

# Part (b) Create Student class, initializer
class Student(Person):
    def __init__(self, email, firstname, lastname):
        self.group = ""
        super(Student, self).__init__(email, firstname, lastname)


# Part (c) Implement load_students() Function
def load_students():
    student_list = []
    try:
        file = open("student.txt", "r")
        contents = file.read()
        student_list = contents.split("\n")
    except IOError:
        print("File is not found")
    finally:
        return student_list


# Part (c) Implement assign_students() Function
def assign_students(instructor, group, students):
    for student in students:
        firstname, lastname, email = student.split(",")
        studentClass = Student(email, firstname, lastname)+
        studentClass.group = group
        instructor.add_student(studentClass)
    print(f"{len(students)} students assigned to " + instructor.get_name()ee)

# Test program
group = 'PT01'
instructor = Instructor('may@gmail.com', 'May', 'Lim')
students = load_students()
assign_students(instructor, group, students)
