from abc import ABC, abstractmethod

from domain.model.current_game import CurrentGame


class GameService(ABC):

    @abstractmethod
    def create_game(
        self,
        player_id: str,
        with_computer: bool,
    ) -> CurrentGame:
        pass

    @abstractmethod
    def get_available_games(
        self,
    ) -> list[CurrentGame]:
        pass

    @abstractmethod
    def join_game(
        self,
        game_id: str,
        player_id: str,
    ) -> CurrentGame:
        pass

    @abstractmethod
    def get_game(
        self,
        game_id: str,
    ) -> CurrentGame | None:
        pass

    @abstractmethod
    def make_move(
        self,
        current_game: CurrentGame,
        player_id: str,
        row: int,
        column: int,
    ) -> CurrentGame:
        pass

    @abstractmethod
    def make_computer_move(
        self,
        current_game: CurrentGame,
    ) -> CurrentGame:
        pass

    @abstractmethod
    def validate_board(
        self,
        current_game: CurrentGame,
    ) -> bool:
        pass

    @abstractmethod
    def is_game_finished(
        self,
        current_game: CurrentGame,
    ) -> bool:
        pass
