import base64
from functools import wraps

from flask import request, jsonify


class UserAuthenticator:

    def __init__(
        self,
        auth_service,
    ):
        self._auth_service = auth_service

    def required(self, function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            authorization = request.headers.get("Authorization")

            if authorization is None:
                return jsonify({"error": "Authorization required"}), 401

            if not authorization.startswith("Basic "):
                return jsonify({"error": "Invalid authorization format"}), 401

            encoded_credentials = authorization.split(
                " ",
                1,
            )[1]

            try:
                decoded_credentials = base64.b64decode(encoded_credentials).decode(
                    "utf-8"
                )

                login, password = decoded_credentials.split(
                    ":",
                    1,
                )

            except Exception:
                return jsonify({"error": "Invalid credentials"}), 401

            user_id = self._auth_service.sign_in(
                login,
                password,
            )

            if user_id is None:
                return jsonify({"error": "Invalid login or password"}), 401

            request.user_id = user_id

            return function(
                *args,
                **kwargs,
            )

        return wrapper
