def main():
    students = load_result()
    for s in students:
        print(s.name, s.get_score(), "and allocated", s.allocated_school, "the choices are", ", ".join(s.choices))

def byAverage_key(student):
    return student.get_score()

def load_result():
    students = []
    # implement the load result logic here
    try:
        result_object = open("results.txt", "r")
        for line in result_object:
            name, math, chinese, english, science = line.split(",")
            student_instance = Student(name)
            student_instance.math = int(math)
            student_instance.chinese = int(chinese)
            student_instance.english = int(english)
            student_instance.science = int(science)
            student_instance.choices = ["SchoolA", "SchoolB", "SchoolC"]
            students.append(student_instance)
    except IOError:
        print("No result.txt file found. Please create it.")
    # return students
    students = sorted(students, key = byAverage_key, reverse=True)
    x = 0
    for school in ["SchoolA", "SchoolB", "SchoolC"]:
        for i in range(5):
            student = students[x]
            student.allocated_school = school
            students[x] = student
            x += 1
    return students

class Student:
    def __init__(self, name):
        self.name = name
        self.math = 0
        self.chinese = 0
        self.english = 0
        self.science = 0
        self.choices = []
        self.allocated_school = ""

    def get_score(self):
        return (self.math + self.chinese + self.english + self.science) / 4

main()
