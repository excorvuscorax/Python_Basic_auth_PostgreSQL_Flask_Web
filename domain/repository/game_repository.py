from abc import ABC, abstractmethod

from domain.model.current_game import CurrentGame


class GameRepository(ABC):

    @abstractmethod
    def save(
        self,
        game: CurrentGame,
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        game_id: str,
    ) -> CurrentGame | None:
        pass
