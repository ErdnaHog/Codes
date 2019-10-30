from q1Classes import *

lecturer_name = input("Enter Lecturer Name: ")
lecturer_nric = input("Enter Lecturer NRIC: ")
lecturer_id = input("Enter Staff Id: ")
total_TeachingHour = int(input("Enter Total Teaching Hour: "))

lecturer1 = Lecturer(lecturer_name, lecturer_nric, lecturer_id)
lecturer1.set_total_TeachingHour(total_TeachingHour)

student_name = input("Enter Student Name: ")
student_nric = input("Enter Student NRIC: ")
student_admin_no = input("Enter Student admin No: ")
student_test_Mark = int(input("Enter Test mark: "))
student_exam_Mark = int(input("Enter Exan mark: "))

student1 = Student(student_name, student_nric, student_admin_no)
student1.set_test_Mark(student_test_Mark)
student1.set_exam_Mark(student_exam_Mark)

print(lecturer1)
print(student1)
