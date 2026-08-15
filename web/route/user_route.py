from flask import (
    Blueprint,
    jsonify,
)

user_blueprint = Blueprint(
    "user",
    __name__,
)


def register_user_route(
    user_service,
):

    @user_blueprint.route(
        "/users/<user_id>",
        methods=["GET"],
    )
    def get_user(
        user_id,
    ):

        user = user_service.get_user(user_id)

        if user is None:

            return jsonify({"error": "User not found"}), 404

        return jsonify(
            {
                "user_id": user.user_id,
                "login": user.login,
            }
        )

    return user_blueprint
