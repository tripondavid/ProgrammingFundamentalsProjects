from ui.ui import UI
from services import student_service
from repository import student_repo
from domain import student_validator
from repository import student_repository

repo = student_repository.TextFileRepository()
student_service = student_service.StudentService(repo, student_validator.StudentValidator())
ui = UI(student_service)


ui.run_menu()