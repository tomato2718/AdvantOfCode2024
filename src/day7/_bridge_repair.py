__all__ = ["Solution"]

from collections.abc import Iterable
from typing import TypedDict


class _Puzzle(TypedDict):
    target: int
    values: list[int]


class Solution:
    _puzzles: Iterable[_Puzzle]

    def __init__(self, puzzles: Iterable[_Puzzle]) -> None:
        self._puzzles = puzzles

    def calculate_calibration_total(self) -> int:
        total = 0
        for puzzle in self._puzzles:
            if self._is_possible(puzzle):
                total += puzzle["target"]
        return total

    def _is_possible(self, puzzle: _Puzzle) -> bool:
        target, values = puzzle["target"], puzzle["values"]
        is_possible = False
        combination = 2 ** (len(values) - 1)
        for comb in range(combination):
            total = values[0]
            for i in range(1, len(values)):
                if comb & 1:
                    total *= values[i]
                else:
                    total += values[i]
                comb >>= 1
            if total == target:
                is_possible = True
                break
        return is_possible
