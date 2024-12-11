__all__ = ["parse_input"]


def parse_input(path: str) -> list[int]:
    with open(path, "r") as file:
        string = file.read()
    return [int(i) for i in string]
