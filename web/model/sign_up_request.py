from dataclasses import dataclass


@dataclass
class SignUpRequest:

    login: str
    password: str

    @staticmethod
    def from_dict(data: dict):
        return SignUpRequest(
            login=data["login"],
            password=data["password"],
        )
