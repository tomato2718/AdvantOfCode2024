__all__ = ["parse_input"]

from ._warehouse_woes import _Map, _Move


def parse_input(path: str) -> tuple[_Map, list[_Move]]:
    map_ = []
    commands = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            map_.append([i for i in line])
        while line := file.readline().strip("\n"):
            commands.extend(i for i in line)
    return map_, commands
