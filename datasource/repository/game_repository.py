from datasource.database import db

from datasource.mapper.current_game_mapper import CurrentGameMapper

from datasource.model.current_game import (
    CurrentGame as DatasourceCurrentGame,
)

from domain.model.current_game import (
    CurrentGame as DomainCurrentGame,
)


class GameRepository:

    def __init__(
        self,
        mapper: CurrentGameMapper,
    ):
        self._mapper = mapper

    def save(
        self,
        domain_game: DomainCurrentGame,
    ) -> None:

        datasource_game = self._mapper.to_datasource(domain_game)

        existing_game = DatasourceCurrentGame.query.get(datasource_game.game_id)

        if existing_game is None:

            db.session.add(datasource_game)

        else:

            existing_game.board = datasource_game.board

            existing_game.status = datasource_game.status

            existing_game.player1_id = datasource_game.player1_id

            existing_game.player2_id = datasource_game.player2_id

            existing_game.player1_symbol = datasource_game.player1_symbol

            existing_game.player2_symbol = datasource_game.player2_symbol

            existing_game.current_player_id = datasource_game.current_player_id

            existing_game.winner_id = datasource_game.winner_id

        db.session.commit()

    def get(
        self,
        game_id: str,
    ) -> DomainCurrentGame | None:

        datasource_game = DatasourceCurrentGame.query.get(game_id)

        if datasource_game is None:
            return None

        return self._mapper.to_domain(datasource_game)

    def find_waiting_games(
        self,
    ) -> list[DomainCurrentGame]:

        games = DatasourceCurrentGame.query.filter_by(status="WAITING_FOR_PLAYER").all()

        return [self._mapper.to_domain(game) for game in games]
