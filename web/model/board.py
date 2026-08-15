from dataclasses import dataclass


@dataclass
class WebBoard:
    cells: list[int]

    def to_dict(self) -> dict:
        return {"cells": self.cells}

    @staticmethod
    def from_dict(data: dict) -> "WebBoard":
        return WebBoard(cells=data["cells"])
