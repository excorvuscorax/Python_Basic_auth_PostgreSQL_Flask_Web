import uuid

from dataclasses import dataclass, field

from domain.model.board import Board
from domain.model.game_status import GameStatus


def generate_game_id():
    return str(uuid.uuid4())


@dataclass
class CurrentGame:

    game_id: str = field(default_factory=generate_game_id)

    board: Board = field(default_factory=Board)

    status: GameStatus = GameStatus.WAITING_FOR_PLAYER

    player1_id: str | None = None

    player2_id: str | None = None

    player1_symbol: int = 1

    player2_symbol: int = 2

    current_player_id: str | None = None

    winner_id: str | None = None
