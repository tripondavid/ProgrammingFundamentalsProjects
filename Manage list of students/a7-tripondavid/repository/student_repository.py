from domain.student import Student
import pickle

class MemoryRepository:
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


class TextFileRepository(MemoryRepository):
    def __init__(self, file_name = "student.txt"):
        super(TextFileRepository, self).__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        try:
            f = open(self._file_name, "rt")
            lines = f.readlines()
            f.close()
        except IOError:
            raise ValueError("File opening error.")

        for line in lines:
            current_line = line.split(" ")
            name = current_line[1].strip() + " " + current_line[2].strip()
            new_student = Student(int(current_line[0].strip()), name, int(current_line[3].strip()))
            super().add(new_student)

    def _save_file(self):
        try:
            f = open(self._file_name, "w")
            f.write(str(self.data))
            f.close()
        except IOError:
            raise ValueError("File opening error.")


class BinaryFileyRepository(MemoryRepository):
    def __init__(self, file_name = "student.bin"):
        super(BinaryFileyRepository, self).__init__()
        self._file_name = file_name
        self._file_name = file_name
        self._load_file()

    def add(self, new_student: Student):
        super().add(new_student)
        self._save_file()

    def _load_file(self):
        fin = open(self._file_name, "rb")
        obj = pickle.load(fin)

        for c in obj:
            super().add(c)
        fin.close()

    def _save_file(self):
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all(), fout)
        fout.close()



