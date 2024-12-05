__all__ = ["parse_input"]

from ._ceres_search import _XmasChar


def parse_input(path: str) -> list[list[_XmasChar]]:
    puzzle = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            puzzle.append([char for char in line])
    return puzzle
