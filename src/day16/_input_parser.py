__all__ = ["parse_input"]

from typing import cast

from ._reindeer_maze import _CellType, _Map


def parse_input(path: str) -> _Map:
    map_: _Map = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            map_.append([cast(_CellType, cell) for cell in line])
    return map_
