__all__ = ["parse_input"]

from ._hoof_it import _Map


def parse_input(path: str) -> _Map:
    _map = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            _map.append([int(i) for i in line])
    return _map
