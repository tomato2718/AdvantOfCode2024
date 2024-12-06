__all__ = ["parse_input"]


_Orders = list[tuple[int, int]]
_Updates = list[list[int]]


def parse_input(path: str) -> tuple[_Orders, _Updates]:
    orders = []
    updates = []
    with open(path, "r") as file:
        while line := file.readline().strip("\n"):
            order = line.split("|")
            orders.append((int(order[0]), int(order[1])))
        while line := file.readline().strip("\n"):
            updates.append([int(i) for i in line.split(",")])
    return (orders, updates)
