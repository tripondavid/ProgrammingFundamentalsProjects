class Student:
    def __init__(self, student_id: int, student_name: str, student_group: int):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__student_group = student_group

    @property
    def student_id(self):
        return self.__student_id


    @student_id.setter
    def student_id(self, new_value):
        self.__student_id = new_value


    @property
    def student_name(self):
        return self.__student_name

    @property
    def student_group(self):
        return self.__student_group


    @student_group.setter
    def student_group(self, new_value):
        self.__student_group = new_value


    def __str__(self):
        return str(self.student_id) + " " + self.student_name + " " + str(self.student_group)



def test_student():
    new_student = Student(1234, "Tripon David", 917)
    assert new_student.student_id == 1234
    assert new_student.student_name == "Tripon David"
    assert new_student.student_group == 917
    new_student.student_id = 2
    assert new_student.student_id == 2
    new_student.student_group = 916
    assert new_student.student_group == 916


test_student()



