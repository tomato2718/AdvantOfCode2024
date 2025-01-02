__all__ = ["Solution"]

from heapq import heappop, heappush
from sys import maxsize
from typing import Literal

_CellType = Literal[".", "#", "S", "E"]
_Map = list[list[_CellType]]


class Solution:
    @staticmethod
    def find_minimum_costs(__map: _Map) -> int:
        astar = AStar(__map)
        end = astar.simulate()
        return end.cost


class AStar:
    _map: list[list["Cell"]]
    _start: "Cell"
    _end: "Cell"
    _to_test: "PriorityQueue"

    def __init__(self, __map: _Map) -> None:
        self._analyze_map(__map)
        self._to_test = PriorityQueue()
        self._to_test.push(self._start, self._start.distance_to(self._end))

    def _analyze_map(self, __map: _Map) -> None:
        analyzed_map = []
        for row_index, row in enumerate(__map):
            analyzed_row = []
            for col_index, col in enumerate(row):
                cell = Cell((row_index, col_index), cell_type=col)
                match col:
                    case "S":
                        cell.set_prev(analyzed_row[-1])
                        self._start = cell
                    case "E":
                        self._end = cell
                analyzed_row.append(cell)
            analyzed_map.append(analyzed_row)
        self._map = analyzed_map

    def simulate(self) -> "Cell":
        while not self._to_test.is_empty():
            current = self._to_test.pop()
            if current == self._end:
                self._map[self._end.coordinate[0]][self._end.coordinate[1]] = current
                break
            for next_cell in self._get_possible_cells(current):
                if (
                    self._map[next_cell.coordinate[0]][next_cell.coordinate[1]].cost
                    > next_cell.cost
                ):
                    self._map[next_cell.coordinate[0]][next_cell.coordinate[1]] = (
                        next_cell
                    )
                    self._to_test.push(
                        next_cell,
                        self._estimate_cost(next_cell),
                    )
        return self._map[self._end.coordinate[0]][self._end.coordinate[1]]

    def _get_possible_cells(self, cell: "Cell") -> list["Cell"]:
        coordinates_around = [
            (cell.coordinate[0] - 1, cell.coordinate[1]),
            (cell.coordinate[0], cell.coordinate[1] - 1),
            (cell.coordinate[0] + 1, cell.coordinate[1]),
            (cell.coordinate[0], cell.coordinate[1] + 1),
        ]
        possible_cells = []
        for row, col in coordinates_around:
            if (
                (0 <= row <= len(self._map) - 1)
                and (0 <= col <= len(self._map[0]) - 1)
                and self._map[row][col].cell_type in {".", "E"}
            ):
                new_cell = Cell((row, col), cell_type=".")
                new_cell.set_prev(cell)
                possible_cells.append(new_cell)
        return possible_cells

    def _estimate_cost(self, __current: "Cell") -> int:
        return __current.cost + __current.distance_to(self._end)


class Cell:
    coordinate: tuple[int, int]
    cell_type: _CellType
    cost: int
    prev: "Cell | None"

    def __init__(self, __coordinate: tuple[int, int], *, cell_type: _CellType) -> None:
        self.coordinate = __coordinate
        self.cell_type = cell_type
        self.prev = None
        self._update_cost()

    def __eq__(self, value: "Cell") -> bool:
        return self.coordinate == value.coordinate

    def set_prev(self, prev: "Cell") -> None:
        self.prev = prev
        self._update_cost()

    def _update_cost(self) -> None:
        if self.prev is None:
            self.cost = maxsize
        elif self.prev.prev is None:
            self.cost = 0
        elif (
            self.coordinate[0] - self.prev.coordinate[0]
            == self.prev.coordinate[0] - self.prev.prev.coordinate[0]
            and self.coordinate[1] - self.prev.coordinate[1]
            == self.prev.coordinate[1] - self.prev.prev.coordinate[1]
        ):
            self.cost = self.prev.cost + 1
        else:
            self.cost = self.prev.cost + 1001

    def distance_to(self, target: "Cell") -> int:
        return abs(self.coordinate[0] - target.coordinate[0]) + abs(
            self.coordinate[1] - target.coordinate[1]
        )


class PriorityQueue:
    _heap: list[tuple[int, int, "Cell"]]

    def __init__(self) -> None:
        self._heap = []

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def push(self, coordinate: "Cell", cost: int) -> None:
        heappush(self._heap, (cost, id(coordinate), coordinate))

    def pop(self) -> "Cell":
        _, _, coordinate = heappop(self._heap)
        return coordinate
