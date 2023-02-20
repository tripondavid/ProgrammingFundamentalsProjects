import copy
import random

from domain import student


class StudentService:
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator
        self._history = [copy.deepcopy(repo.get_all())]
        self.generate_ten_students()

    def add_student(self, student_id: int, student_name: str, student_group: int):
        new_student = student.Student(student_id, student_name, student_group)
        self._validator.validate(new_student)
        self._repo.add(new_student)
        self._repo._save_file()
        self._history.append(copy.deepcopy(self._repo.get_all()))


    def get_all_students(self):
        return self._repo.get_all()


    def remove_group(self, stud_group: int):
        list_of_students = self._repo.get_all().copy()
        for id in list_of_students.keys():
            if list_of_students[id].student_group == stud_group:
                self._repo.remove(list_of_students[id].student_id)
        self._history.append(copy.deepcopy(self._repo.get_all()))
        self._repo._save_file()

    def generate_ten_students(self):
        id_number = 1000
        student_first_names = ["David", "Iulius", "Alisa", "Razvan", "Dalia", "Teodora", "Denisa"]
        student_last_names = ["Pop", "Muresan", "Catana", "Costea", "Vancea"]
        student_groups = [911, 912, 913, 914, 915, 916, 917]
        n = 10

        while n > 0:
            rnd = random.randint
            first_name = student_first_names[rnd(0, 5)]
            last_name = student_last_names[rnd(0, 4)]
            group = student_groups[rnd(0, 6)]
            full_name = last_name + " " + first_name
            n = n - 1
            new_student = student.Student(id_number, full_name, group)
            id_number -= 1
            self._repo.add(new_student)
        self._repo._save_file()


    def undo_last_operation(self):
        if len(self._history) == 0:
            raise ValueError("Nothing to undo. ")
        self._history.pop()
        self._repo.undo(self._history[-1])
        self._repo._save_file()