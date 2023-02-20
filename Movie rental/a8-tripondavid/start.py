from ui.ui import UI
from services.client_service import ClientService
from repository.client_repo import ClientRepository
from repository.movie_repo import MovieRepository
from services.movie_service import MovieService
from services.rental_service import RentalService
from repository.rental_repo import RentalRepository
from domain.client_validator import ClientValidator
from domain.movie_validator import MovieValidator
from tests.test_rental import test_rental
from tests.test_add import test_add
from tests.test_remove import test_remove
from tests.test_list import test_list

client_validator = ClientValidator()
movie_validator = MovieValidator()

client_repo = ClientRepository()
movie_repo = MovieRepository()
rental_repo = RentalRepository()


client_service = ClientService(client_repo, client_validator)
movie_service = MovieService(movie_repo, movie_validator)
rental_service = RentalService(rental_repo, movie_repo, client_repo)

ui = UI(client_service, movie_service, rental_service)

test_rental()
test_add()
test_remove()
test_list()

ui.run_menu()