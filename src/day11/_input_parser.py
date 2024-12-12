__all__ = ["parse_input"]


def parse_input(path: str) -> list[int]:
    with open(path, "r") as file:
        line = file.read()
    return [int(num) for num in line.split()]
