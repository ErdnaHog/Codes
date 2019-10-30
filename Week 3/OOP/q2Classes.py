class Person:
    def __init__(self, name, nric):
        self.__name = name
        self.__nric = nric

    def get_name(self):
        return self.__name

    def get_nric(self):
        return self.__nric

    def set_name(self, name):
        self.__name = name

    def set_nric(self, nric):
        self.__nric = nric

class Student(Person):
    def __init__(self, name, nric, admin_no):
        Person.__init__(self, name, nric)
        self.__admin_no = admin_no
        self.__test_Mark = ""
        self.__exam_Mark = ""

    def get_admin_no(self):
        return self.__admin_no

    def get_test_Mark(self):
        return self.__test_Mark

    def get_exam_Mark(self):
        return self.__exam_Mark

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no

    def set_test_Mark(self, test_Mark):
        while test_Mark < 0 or 100 < test_Mark:
            test_Mark = int(input("Enter Test mark: "))
        self.__test_Mark = test_Mark

    def set_exam_Mark(self, exam_Mark):
        while exam_Mark < 0 or 100 < exam_Mark:
            exam_Mark = int(input("Enter Exam mark: "))
        self.__exam_Mark = exam_Mark

    def computeFinalMark(self):
        finalMark = (self.__exam_Mark + self.__test_Mark) / 2
        return finalMark

    def __str__(self):
        s = f"{self.get_name()}, Admin No: {self.get_admin_no()} final mark is {self.computeFinalMark():.2f}"
        return s

class Lecturer(Person):
    def __init__(self, name, nric, staff_id):
        while nric != staff_id:
            staff_id = input("Enter Staff Id: ")
        Person.__init__(self, name, nric)
        # super(Lecturer, self).__init__(name, nric)
        self.__staff_id = staff_id
        # self.__salary = 90
        self.__total_TeachingHour = ""

    def get_staff_id(self):
        return self.__staff_id

    def get_total_TeachingHour(self):
        return self.__total_TeachingHour

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_total_TeachingHour(self, total_TeachingHour):
        self.__total_TeachingHour = total_TeachingHour

    def computeSalary(self):
        return 90 * self.__total_TeachingHour

    def __str__(self):
        s = f"{self.get_name()}, Staff Id: {self.get_staff_id()} earns ${self.computeSalary():.2f}"
        return s
