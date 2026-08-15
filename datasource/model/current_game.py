import uuid

from datasource.database import db


def generate_game_id():
    return str(uuid.uuid4())


class CurrentGame(db.Model):

    __tablename__ = "current_games"

    game_id = db.Column(
        db.String,
        primary_key=True,
        default=generate_game_id,
    )

    board = db.Column(
        db.JSON,
        nullable=False,
    )

    status = db.Column(
        db.String,
        nullable=False,
        default="WAITING_FOR_PLAYER",
    )

    player1_id = db.Column(
        db.String,
        nullable=True,
    )

    player2_id = db.Column(
        db.String,
        nullable=True,
    )

    player1_symbol = db.Column(
        db.Integer,
        nullable=False,
        default=1,
    )

    player2_symbol = db.Column(
        db.Integer,
        nullable=False,
        default=2,
    )

    current_player_id = db.Column(
        db.String,
        nullable=True,
    )

    winner_id = db.Column(
        db.String,
        nullable=True,
    )
