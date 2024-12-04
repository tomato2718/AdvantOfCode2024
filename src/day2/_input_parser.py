__all__ = ["parse_input"]


def parse_input(path: str) -> list[list[int]]:
    lst = []
    with open(path, "r") as file:
        while line := file.readline():
            lst.append([int(i) for i in line.split(" ")])
    return lst
