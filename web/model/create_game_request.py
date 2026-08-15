from dataclasses import dataclass


@dataclass
class CreateGameRequest:

    with_computer: bool = False

    @staticmethod
    def from_dict(data: dict):

        return CreateGameRequest(
            with_computer=data.get(
                "with_computer",
                False,
            )
        )
