__all__ = ["parse_input"]


def parse_input(path: str) -> list[tuple[int, int]]:
    cells = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            x, y = line.split(",")
            cells.append((int(x), int(y)))
    return cells
