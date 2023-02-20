class UI:
    def __init__(self, student_service):
        self._student_service = student_service


    def print_options(self):
        print("1. Press 1 to add a student. ")
        print("2. Press 2 to display the list of students. ")
        print("3. Press 3 to filter the list so that students in a given group are deleted from the list. ")
        print("4. Press 4 to undo the last operation that modified the program data. ")
        print("5. Press 5 to exit the application. ")


    def choose_option(self):
        chosen_option = input("> ")
        return chosen_option


    def run_menu(self):
        while True:
            self.print_options()
            command = self.choose_option()
            if command == "5":
                break
            self.run_chosen_option(command)


    def add_student(self):
        student_id = int(input("Enter the ID: "))
        student_name = input("Enter the full name: ")
        student_group = int(input("Enter the group: "))
        try:
            self._student_service.add_student(student_id, student_name, student_group)
        except ValueError:
            pass


    def display_all_students(self):
        print(self._student_service.get_all_students())


    def filter_list(self):
        student_group = int(input("Enter the group: "))
        try:
            self._student_service.remove_group(student_group)
        except ValueError:
            print("Wrong input for filter_list")

    def undo_function(self):
        self._student_service.undo_last_operation()


    def run_chosen_option(self, chosen_option):
        match chosen_option:
            case "1":
                self.add_student()
            case "2":
                self.display_all_students()
            case "3":
                self.filter_list()
            case "4":
                self.undo_function()
            case _:
                print("Invalid command")
