from datasource.repository.user_repository import UserRepository

from domain.model.user import User
from domain.service.user_service import UserService


class UserServiceImpl(UserService):

    def __init__(
        self,
        repository: UserRepository,
    ):
        self._repository = repository

    def create_user(
        self,
        login: str,
        password: str,
    ) -> bool:

        if self._repository.find_by_login(login):
            return False

        user = User(
            login=login,
            password=password,
        )

        self._repository.save(user)

        return True

    def find_by_login(
        self,
        login: str,
    ) -> User | None:

        return self._repository.find_by_login(login)

    def find_by_id(
        self,
        user_id: str,
    ) -> User | None:

        return self._repository.find_by_id(user_id)

    def authenticate(
        self,
        login: str,
        password: str,
    ) -> User | None:

        user = self.find_by_login(login)

        if user is None:
            return None

        if user.password != password:
            return None

        return user
