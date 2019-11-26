from Course import Course

course1 = Course('ITDF08', 'Diploma in Financial Informatics', '70')

print(f"The student intake for {course1.get_course_name()}({course1.get_course_code()}) is {course1.get_intake_number()}")
