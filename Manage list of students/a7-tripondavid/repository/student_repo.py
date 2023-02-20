from domain.student import Student
class TestRepo:

    def __init__(self):
        self.data = {}

    def add(self, new_student: Student):
        self.data[new_student.student_id] = new_student

    def get_all(self):
        return self.data

    def remove(self, id: int):
        del self.data[id]

    def undo(self, old_data):
        self.data = old_data