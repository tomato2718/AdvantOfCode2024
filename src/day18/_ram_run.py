__all__ = ["Solution"]

from heapq import heappop, heappush
from sys import maxsize
from typing import Literal

_Cell = Literal[".", "#"]
_Map = list[list[_Cell]]


class Solution:
    @staticmethod
    def find_minimum_steps(corruppted_cells: list[tuple[int, int]], size: int) -> int:
        map_: _Map = [["." for _ in range(size + 1)] for _ in range(size + 1)]
        for x, y in corruppted_cells:
            map_[x][y] = "#"
        a_star = AStar(
            map_,
            start=Coordinate(0, 0),
            end=Coordinate(size, size),
        )
        res = a_star.simulate()
        return res if res != maxsize else -1

    @classmethod
    def find_first_cell_block_exit(
        cls, corruppted_cells: list[tuple[int, int]], size: int
    ) -> tuple[int, int]:
        start, end = 0, len(corruppted_cells) - 1
        while True:
            mid = (start + end) // 2
            cur = cls.find_minimum_steps(corruppted_cells[:mid], size=size)
            next_ = cls.find_minimum_steps(corruppted_cells[: mid + 1], size=size)
            if cur == next_ == -1:
                end = (mid + end) // 2
            elif cur != -1 and next_ != -1:
                start = (start + mid) // 2
            else:
                break
        return corruppted_cells[mid]


class AStar:
    _map: _Map
    _start: "Coordinate"
    _end: "Coordinate"
    _to_test: "PriorityQueue"
    _steps: list[list[int]]

    def __init__(self, __map: _Map, *, start: "Coordinate", end: "Coordinate") -> None:
        self._map = __map
        self._start = start
        self._end = end
        self._to_test = PriorityQueue()
        self._to_test.push(start, start.distance_to(end))
        self._steps = [[maxsize for _ in row] for row in __map]
        self._steps[start.row][start.col] = 0

    def simulate(self) -> int:
        while not self._to_test.is_empty():
            current = self._to_test.pop()
            if current == self._end:
                break
            for next_cell in self._get_possible_cells(current):
                self._steps[next_cell.row][next_cell.col] = (
                    self._steps[current.row][current.col] + 1
                )
                self._to_test.push(
                    next_cell,
                    self._estimate_cost(current, next_cell),
                )
        return self._steps[self._end.row][self._end.col]

    def _get_possible_cells(self, coordinate: "Coordinate") -> list["Coordinate"]:
        cells_around = [
            (coordinate.row - 1, coordinate.col),
            (coordinate.row, coordinate.col - 1),
            (coordinate.row + 1, coordinate.col),
            (coordinate.row, coordinate.col + 1),
        ]
        possible_cells = []
        current_steps = self._steps[coordinate.row][coordinate.col] + 1
        for row, col in cells_around:
            if (
                (0 <= row <= len(self._map) - 1)
                and (0 <= col <= len(self._map[0]) - 1)
                and self._map[row][col] == "."
                and current_steps < self._steps[row][col]
            ):
                possible_cells.append(Coordinate(row, col))
        return possible_cells

    def _estimate_cost(self, __current: "Coordinate", __next: "Coordinate") -> int:
        return (
            self._steps[__current.row][__current.col]
            + 1
            + __next.distance_to(self._end)
        )


class Coordinate:
    row: int
    col: int

    def __init__(self, __row: int, __col: int) -> None:
        self.row = __row
        self.col = __col

    def __eq__(self, value: "Coordinate") -> bool:
        return (self.row, self.col) == (value.row, value.col)

    def distance_to(self, target: "Coordinate") -> int:
        return abs(target.col - self.col) + abs(target.row - self.row)


class PriorityQueue:
    _heap: list[tuple[int, int, "Coordinate"]]

    def __init__(self) -> None:
        self._heap = []

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def push(self, coordinate: "Coordinate", cost: int) -> None:
        heappush(self._heap, (cost, id(coordinate), coordinate))

    def pop(self) -> "Coordinate":
        _, _, coordinate = heappop(self._heap)
        return coordinate
