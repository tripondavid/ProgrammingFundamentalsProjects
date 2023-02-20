from ui.ui import UI
from services.client_service import ClientService
from repository.client_repo import ClientRepository
from repository.movie_repo import MovieRepository
from services.movie_service import MovieService
from services.rental_service import RentalService
from repository.rental_repo import RentalRepository
from domain.client_validator import ClientValidator
from domain.movie_validator import MovieValidator


def test_rental():
    test_client_validator = ClientValidator()
    test_movie_validator = MovieValidator()

    test_client_repo = ClientRepository()
    test_movie_repo = MovieRepository()
    test_rental_repo = RentalRepository()

    test_client_service = ClientService(test_client_repo, test_client_validator)
    test_movie_service = MovieService(test_movie_repo, test_movie_validator)
    test_rental_service = RentalService(test_rental_repo, test_movie_repo, test_client_repo)

    test_movie_service.add_movie(1, "Bad Boys", "Cops", "Action")
    test_client_service.add_client(1, "Tripon David")
    test_rental_service.add_rental(1,1,1,"2022-12-26","2022-12-29")
    test_rental_service.return_rental(1)
    test_rental_service.add_rental(2,1,1,"2023-12-27","2023-12-28")
    test_rental_service.most_rented_movies()
    test_rental_service.most_active_clients()

