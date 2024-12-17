__all__ = ["parse_input"]

from ._claw_contraption import _Equotation


def parse_input(path: str) -> list[tuple[_Equotation, _Equotation]]:
    with open(path, "r") as file:
        blocks = file.read().split("\n\n")
    puzzles = []
    for block in blocks:
        e1 = []
        e2 = []
        parsed_block = (
            block.replace("Button A", "")
            .replace("Button B", "")
            .replace("Prize", "")
            .replace("X", "")
            .replace("Y", "")
            .replace(": ", "")
            .replace("+", "")
            .replace("=", "")
        ).split("\n")
        for line in parsed_block:
            a, b = line.split(", ")
            e1.append(int(a))
            e2.append(int(b))
        puzzles.append((tuple(e1), tuple(e2)))
    return puzzles
