from abc import ABC, abstractmethod

from web.model.sign_up_request import SignUpRequest


class AuthService(ABC):

    @abstractmethod
    def sign_up(
        self,
        request: SignUpRequest,
    ) -> bool:
        pass

    @abstractmethod
    def sign_in(
        self,
        login: str,
        password: str,
    ) -> str | None:
        pass
