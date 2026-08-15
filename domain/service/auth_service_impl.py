from domain.service.auth_service import AuthService
from domain.service.user_service import UserService


class AuthServiceImpl(AuthService):

    def __init__(
        self,
        user_service: UserService,
    ):
        self._user_service = user_service

    def sign_up(
        self,
        request,
    ) -> bool:

        return self._user_service.create_user(
            request.login,
            request.password,
        )

    def sign_in(
        self,
        login: str,
        password: str,
    ) -> str | None:

        user = self._user_service.authenticate(
            login,
            password,
        )

        if user is None:
            return None

        return user.user_id
