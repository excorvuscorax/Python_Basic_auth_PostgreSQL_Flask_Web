from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
)

from web.model.current_game import WebCurrentGame
from web.mapper.current_game_mapper import (
    to_domain,
    to_web,
)

game_blueprint = Blueprint(
    "game",
    __name__,
)


def register_game_route(
    service,
    authenticator,
):

    @game_blueprint.route(
        "/game",
        methods=["GET"],
    )
    def game_page():

        return render_template("game.html")

    @game_blueprint.route(
        "/games/create",
        methods=["POST"],
    )
    @authenticator.required
    def create_game():

        data = request.get_json(silent=True)

        with_computer = False

        if data:

            with_computer = data.get(
                "with_computer",
                False,
            )

        game = service.create_game(
            request.user_id,
            with_computer,
        )

        result = to_web(game)

        return jsonify(result.to_dict())

    @game_blueprint.route(
        "/games",
        methods=["GET"],
    )
    @authenticator.required
    def get_games():

        games = service.get_available_games()

        return jsonify([to_web(game).to_dict() for game in games])

    @game_blueprint.route(
        "/games/<game_id>/join",
        methods=["POST"],
    )
    @authenticator.required
    def join_game(
        game_id,
    ):

        try:

            game = service.join_game(
                game_id,
                request.user_id,
            )

            return jsonify(to_web(game).to_dict())

        except Exception as error:

            return jsonify({"error": str(error)}), 400

    @game_blueprint.route(
        "/games/<game_id>",
        methods=["GET"],
    )
    @authenticator.required
    def get_game(
        game_id,
    ):

        game = service.get_game(game_id)

        if game is None:

            return jsonify({"error": "Game not found"}), 404

        return jsonify(to_web(game).to_dict())

    @game_blueprint.route(
        "/games/<game_id>/move",
        methods=["POST"],
    )
    @authenticator.required
    def make_move(
        game_id,
    ):

        data = request.get_json()

        game = service.get_game(game_id)

        if game is None:

            return jsonify({"error": "Game not found"}), 404

        try:

            updated_game = service.make_move(
                game,
                request.user_id,
                data["row"],
                data["column"],
            )

            # Если игра против компьютера
            if updated_game.player2_id == "computer":

                updated_game = service.make_computer_move(updated_game)

            return jsonify(to_web(updated_game).to_dict())

        except Exception as error:

            return jsonify({"error": str(error)}), 400

    return game_blueprint
