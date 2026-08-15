from dataclasses import dataclass

from web.model.board import WebBoard


@dataclass
class WebCurrentGame:

    game_id: str

    board: WebBoard

    status: str

    player1_id: str | None

    player2_id: str | None

    player1_symbol: int

    player2_symbol: int

    current_player_id: str | None

    winner_id: str | None

    def to_dict(self) -> dict:

        return {
            "game_id": self.game_id,
            "board": self.board.to_dict(),
            "status": self.status,
            "player1_id": self.player1_id,
            "player2_id": self.player2_id,
            "player1_symbol": self.player1_symbol,
            "player2_symbol": self.player2_symbol,
            "current_player_id": self.current_player_id,
            "winner_id": self.winner_id,
        }

    @staticmethod
    def from_dict(
        data: dict,
    ) -> "WebCurrentGame":

        return WebCurrentGame(
            game_id=data.get(
                "game_id",
                "",
            ),
            board=WebBoard.from_dict(data["board"]),
            status=data.get(
                "status",
                "",
            ),
            player1_id=data.get("player1_id"),
            player2_id=data.get("player2_id"),
            player1_symbol=data.get(
                "player1_symbol",
                1,
            ),
            player2_symbol=data.get(
                "player2_symbol",
                2,
            ),
            current_player_id=data.get("current_player_id"),
            winner_id=data.get("winner_id"),
        )
