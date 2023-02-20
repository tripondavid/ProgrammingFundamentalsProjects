from ui.ui import UI
from services.battle_service import BattleService
from domain.battlefield import BattleField
from services.battle_service import ComputerService

player_battlefield = BattleField()
computer_battlefield = BattleField()

computer = ComputerService(player_battlefield)

service = BattleService(player_battlefield, computer_battlefield, computer)

ui = UI(service, computer)

ui.start()
