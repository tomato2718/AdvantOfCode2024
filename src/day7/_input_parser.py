__all__ = ["parse_input"]

from ._bridge_repair import _Puzzle


def parse_input(path: str) -> list[_Puzzle]:
    puzzles = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            lst = line.split(":")
            puzzle = _Puzzle(
                target=int(lst[0]), values=[int(i) for i in lst[1].strip().split(" ")]
            )
            puzzles.append(puzzle)

    return puzzles
