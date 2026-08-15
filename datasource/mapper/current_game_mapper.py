from datasource.model.current_game import (
    CurrentGame as DatasourceCurrentGame,
)

from domain.model.board import Board as DomainBoard
from domain.model.current_game import (
    CurrentGame as DomainCurrentGame,
)

from domain.model.game_status import GameStatus


class CurrentGameMapper:

    def to_datasource(
        self,
        domain_game: DomainCurrentGame,
    ) -> DatasourceCurrentGame:

        return DatasourceCurrentGame(
            game_id=domain_game.game_id,
            board=domain_game.board.cells,
            status=domain_game.status.value,
            player1_id=domain_game.player1_id,
            player2_id=domain_game.player2_id,
            player1_symbol=domain_game.player1_symbol,
            player2_symbol=domain_game.player2_symbol,
            current_player_id=domain_game.current_player_id,
            winner_id=domain_game.winner_id,
        )

    def to_domain(
        self,
        datasource_game: DatasourceCurrentGame,
    ) -> DomainCurrentGame:

        return DomainCurrentGame(
            game_id=datasource_game.game_id,
            board=DomainBoard(
                cells=datasource_game.board,
            ),
            status=GameStatus(datasource_game.status),
            player1_id=datasource_game.player1_id,
            player2_id=datasource_game.player2_id,
            player1_symbol=(datasource_game.player1_symbol),
            player2_symbol=(datasource_game.player2_symbol),
            current_player_id=(datasource_game.current_player_id),
            winner_id=datasource_game.winner_id,
        )
