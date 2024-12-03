__all__ = ["parse_day1_input", "parse_day2_input"]


def parse_day1_input(path: str) -> tuple[list[int], list[int]]:
    lst1, lst2 = [], []
    with open(path, "r") as file:
        while line := file.readline():
            a, b = eval(line.strip().replace("   ", ", "))
            lst1.append(a)
            lst2.append(b)
    return (lst1, lst2)


def parse_day2_input(path: str) -> list[list[int]]:
    lst = []
    with open(path, "r") as file:
        while line := file.readline():
            lst.append([int(i) for i in line.split(" ")])
    return lst
