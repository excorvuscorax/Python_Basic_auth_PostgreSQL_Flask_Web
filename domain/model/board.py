from dataclasses import dataclass, field

EMPTY = 0
HUMAN = 1
COMPUTER = 2

BOARD_SIZE = 3


@dataclass
class Board:
    cells: list[list[int]] = field(
        default_factory=lambda: [
            [EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
        ]
    )
