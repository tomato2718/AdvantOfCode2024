__all__ = ["Solution"]

from typing import Literal, TypedDict

_Cell = Literal[".", "#", "^"]
_Map = list[list[_Cell]]
_Coordinate = tuple[int, int]
_Direction = Literal["N", "E", "S", "W"]


class _AnalyzeResult(TypedDict):
    guards: _Coordinate
    obstables: set[_Coordinate]


class Solution:
    _map: _Map

    def __init__(self, map_: _Map) -> None:
        self._map = map_
        self._map_analysis = self._analyze_map(map_)

    def _analyze_map(self, map_: _Map) -> _AnalyzeResult:
        result = _AnalyzeResult(guards=tuple(), obstables=set())
        for y, row in enumerate(map_):
            for x, cell in enumerate(row):
                match cell:
                    case "#":
                        result["obstables"].add((x, y))
                    case "^":
                        result["guards"] = (x, y)
                    case _:
                        pass
        return result

    def get_visited_positions(self) -> int:
        guard = Guard(self._map_analysis["guards"])
        visited = set()

        while True:
            visited.add(guard.current_coordinate())
            next_move = guard.next_coordinate()

            if self._is_obstacle(next_move):
                guard.turn_right()
            elif self._is_exceeding_map(next_move):
                break
            else:
                guard.move()

        return len(visited)

    def _is_obstacle(self, coordinate: _Coordinate) -> bool:
        return coordinate in self._map_analysis["obstables"]

    def _is_exceeding_map(self, coordinate: _Coordinate) -> bool:
        return (
            coordinate[0] < 0
            or coordinate[1] < 0
            or coordinate[0] == len(self._map[0])
            or coordinate[1] == len(self._map)
        )


class Guard:
    _coordinate: _Coordinate
    _direction: _Direction

    def __init__(self, coordinate: _Coordinate) -> None:
        self._coordinate = coordinate
        self._direction = "N"

    def current_coordinate(self) -> _Coordinate:
        return self._coordinate

    def next_coordinate(self) -> _Coordinate:
        match self._direction:
            case "N":
                return (self._coordinate[0], self._coordinate[1] - 1)
            case "E":
                return (self._coordinate[0] + 1, self._coordinate[1])
            case "W":
                return (self._coordinate[0] - 1, self._coordinate[1])
            case "S":
                return (self._coordinate[0], self._coordinate[1] + 1)

    def move(self) -> None:
        self._coordinate = self.next_coordinate()

    def turn_right(self) -> None:
        match self._direction:
            case "N":
                self._direction = "E"
            case "E":
                self._direction = "S"
            case "S":
                self._direction = "W"
            case "W":
                self._direction = "N"
