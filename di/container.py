from datasource.mapper.current_game_mapper import CurrentGameMapper
from datasource.repository.game_repository import GameRepository

from datasource.mapper.user_mapper import UserMapper
from datasource.repository.user_repository import UserRepository

from domain.service.game_service_impl import GameServiceImpl
from domain.service.user_service_impl import UserServiceImpl

from domain.service.auth_service_impl import AuthServiceImpl
from web.authenticator.user_authenticator import UserAuthenticator


class Container:

    def __init__(self):

        self.game_mapper = CurrentGameMapper()

        self.game_repository = GameRepository(self.game_mapper)

        self.game_service = GameServiceImpl(self.game_repository)

        self.user_mapper = UserMapper()

        self.user_repository = UserRepository(self.user_mapper)

        self.user_service = UserServiceImpl(self.user_repository)
        self.auth_service = AuthServiceImpl(self.user_service)
        self.authenticator = UserAuthenticator(self.auth_service)
