from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
)

from web.model.sign_up_request import SignUpRequest

auth_blueprint = Blueprint(
    "auth",
    __name__,
)


def register_auth_route(auth_service):

    @auth_blueprint.route(
        "/",
        methods=["GET"],
    )
    def auth_page():
        return render_template("auth.html")

    @auth_blueprint.route(
        "/signup",
        methods=["POST"],
    )
    def signup():

        data = request.get_json(silent=True)

        if data is None:
            data = request.form.to_dict()

        if not data:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Empty request",
                    }
                ),
                400,
            )

        request_model = SignUpRequest.from_dict(data)

        result = auth_service.sign_up(
            request_model,
        )

        return jsonify(
            {
                "success": result,
            }
        )

    @auth_blueprint.route(
        "/login",
        methods=["POST"],
    )
    def login():

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Authorization header missing",
                    }
                ),
                401,
            )

        try:
            auth_type, encoded_credentials = auth_header.split(
                " ",
                1,
            )

            if auth_type != "Basic":
                raise ValueError

            import base64

            decoded = base64.b64decode(encoded_credentials).decode("utf-8")

            login, password = decoded.split(
                ":",
                1,
            )

        except Exception:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Invalid authorization format",
                    }
                ),
                401,
            )

        user_id = auth_service.sign_in(
            login,
            password,
        )

        if user_id is None:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "Invalid login or password",
                    }
                ),
                401,
            )

        return jsonify(
            {
                "success": True,
                "user_id": user_id,
            }
        )

    return auth_blueprint
