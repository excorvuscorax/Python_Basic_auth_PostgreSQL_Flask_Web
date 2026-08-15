from dataclasses import dataclass


@dataclass
class MoveRequest:

    row: int
    column: int

    @staticmethod
    def from_dict(data: dict):

        return MoveRequest(
            row=data["row"],
            column=data["column"],
        )
