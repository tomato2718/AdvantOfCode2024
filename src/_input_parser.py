__all__ = ["parse_input"]


def parse_input(path: str) -> tuple[list[int], list[int]]:
    lst1, lst2 = [], []
    with open(path, "r") as file:
        while line := file.readline():
            a, b = eval(line.strip().replace("   ", ", "))
            lst1.append(a)
            lst2.append(b)
    return (lst1, lst2)
