# Name: Bostero, Alexa C.

class Student_acb:
    def __init__(self, name_acb, student_id_acb, course_acb):
        self.name_acb = name_acb
        self.student_id_acb = student_id_acb
        self.course_acb = course_acb

    def display_student_acb(self):
        print("Name:", self.name_acb)
        print("Student ID:", self.student_id_acb)
        print("Course:", self.course_acb)


student1_acb = Student_acb("Maria", "2023-001", "BSIS")
student1_acb.display_student_acb()