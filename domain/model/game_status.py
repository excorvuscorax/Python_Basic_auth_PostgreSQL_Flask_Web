from enum import Enum


class GameStatus(Enum):

    WAITING_FOR_PLAYER = "WAITING_FOR_PLAYER"

    PLAYER_TURN = "PLAYER_TURN"

    DRAW = "DRAW"

    PLAYER_WON = "PLAYER_WON"
