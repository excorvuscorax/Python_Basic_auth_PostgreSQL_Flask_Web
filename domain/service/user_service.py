from abc import ABC, abstractmethod

from domain.model.user import User


class UserService(ABC):

    @abstractmethod
    def create_user(
        self,
        login: str,
        password: str,
    ) -> bool:
        pass

    @abstractmethod
    def find_by_login(
        self,
        login: str,
    ) -> User | None:
        pass

    @abstractmethod
    def find_by_id(
        self,
        user_id: str,
    ) -> User | None:
        pass

    @abstractmethod
    def authenticate(
        self,
        login: str,
        password: str,
    ) -> User | None:
        pass
