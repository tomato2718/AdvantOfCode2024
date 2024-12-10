__all__ = ["Solution"]

from itertools import combinations
from typing import Literal

_EmptyCell = Literal["."]
_Antenna = str
_Cell = _Antenna | _EmptyCell
_Map = list[list[_Cell]]
_Coordinate = tuple[int, int]
_AnalyzeResult = dict[_Antenna, set[_Coordinate]]


class Solution:
    _map: _Map
    _map_analysis: _AnalyzeResult

    def __init__(self, map_: _Map) -> None:
        self._map = map_
        self._map_analysis = self._analyze_map(map_)

    def _analyze_map(self, map_: _Map) -> _AnalyzeResult:
        result: _AnalyzeResult = {}
        for y, row in enumerate(map_):
            for x, cell in enumerate(row):
                if cell == ".":
                    continue
                if cell not in result:
                    result[cell] = {(x, y)}
                else:
                    result[cell].add((x, y))
        return result

    def count_closest_antinodes(self) -> int:
        result: set[_Coordinate] = set()
        for coordinates in self._map_analysis.values():
            for c1, c2 in combinations(coordinates, 2):
                antinodes = self._calculate_antinodes(c1, c2)
                if antinodes:
                    result.add(antinodes[0])
                antinodes = self._calculate_antinodes(c2, c1)
                if antinodes:
                    result.add(antinodes[0])
        return len(result)

    def count_all_antinodes(self) -> int:
        result: set[_Coordinate] = set()
        for coordinates in self._map_analysis.values():
            for c1, c2 in combinations(coordinates, 2):
                antinodes = (
                    [c1, c2]
                    + self._calculate_antinodes(c1, c2)
                    + self._calculate_antinodes(c2, c1)
                )
                for antinode in antinodes:
                    result.add(antinode)
        return len(result)

    def _calculate_antinodes(self, a: _Coordinate, b: _Coordinate) -> list[_Coordinate]:
        antinodes = []
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        multiply = 1
        while self._is_within_bound(c := (b[0] + dx * multiply, b[1] + dy * multiply)):
            antinodes.append(c)
            multiply += 1
        return antinodes

    def _is_within_bound(self, coordinate: _Coordinate) -> bool:
        x, y = coordinate
        return 0 <= x < len(self._map[0]) and 0 <= y < len(self._map)
