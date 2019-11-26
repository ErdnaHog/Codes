class Course:
    def __init__(self, course_code, course_name, intake_number):
        # self.__course_code = ""
        self.set_course_code(course_code)
        self.__course_name = course_name
        self.__intake_number = intake_number

    def get_course_code(self):
        return self.__course_code

    def get_course_name(self):
        return self.__course_name

    def get_intake_number(self):
        return self.__intake_number

    def set_course_code(self, course_code):
        while len(course_code) != 6:
            print("Course code is incorrect!")
            course_code = input("Enter course code: ")
        self.__course_code = course_code

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def set_intake_number(self, intake_number):
        self.__intake_number = intake_number



