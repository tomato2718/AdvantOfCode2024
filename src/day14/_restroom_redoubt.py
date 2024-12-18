__all__ = ["Solution"]

from collections.abc import Iterable
from math import prod
from typing import TypedDict


class _Robot(TypedDict):
    position: tuple[int, int]
    velocity: tuple[int, int]


_MapSize = tuple[int, int]


class Solution:
    _robots: Iterable[_Robot]
    _map_size: _MapSize
    map: list[list[int]]

    def __init__(self, robots: Iterable[_Robot], map_size: _MapSize) -> None:
        self._robots = robots
        self._map_size = map_size
        self._mid = ((self._map_size[0] - 1) / 2, (self._map_size[1] - 1) / 2)
        self.map = [[0] * map_size[0] for _ in range(map_size[1])]

    def calculate_safety_factor(self, seconds: int) -> int:
        quadrant_total = [0] * 5
        for robot in self._robots:
            position = self._simulate(robot["position"], robot["velocity"], seconds)
            self.map[position[1]][position[0]] += 1
            quadrant_total[self._quadrant(position)] += 1

        return prod(quadrant_total[:4])

    def _simulate(
        self, start: tuple[int, int], move: tuple[int, int], times: int
    ) -> tuple[int, int]:
        x, y = (
            (start[0] + move[0] * times) % self._map_size[0],
            (start[1] + move[1] * times) % self._map_size[1],
        )
        return x, y

    def _quadrant(self, position: tuple[int, int]) -> int:
        if position[0] == self._mid[0] or position[1] == self._mid[1]:
            return 4

        if position[0] < self._mid[0]:
            if position[1] < self._mid[1]:
                return 0
            else:
                return 1
        else:
            if position[1] < self._mid[1]:
                return 2
            else:
                return 3
