from ui.ui import UI
from repository.repo import Repo
from services.service import Service

repo = Repo()

service = Service(repo)

ui = UI(service)

ui.run_menu()

