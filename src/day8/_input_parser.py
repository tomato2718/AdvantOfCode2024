__all__ = ["parse_input"]

from ._resonant_collinearity import _Map


def parse_input(path: str) -> _Map:
    map_ = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            map_.append([i for i in line])
    return map_
