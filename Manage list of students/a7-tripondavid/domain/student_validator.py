from domain import student
class StudentValidator:

    def validate(self, student: student.Student):
        index = student.student_name.find(" ")
        if index == -1:
            raise ValueError("Full name needed.")
        for i in range(len(student.student_name)):
            if student.student_name[i].isdigit():
                raise ValueError("Wrong name.")