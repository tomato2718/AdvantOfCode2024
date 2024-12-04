__all__ = ["parse_input"]


def parse_input(path: str) -> str:
    with open(path, "r") as file:
        string = file.read()
    return string
