__all__ = ["Solution", "Operator"]

from collections.abc import Iterable
from itertools import product
from math import floor, log10
from typing import Callable, TypedDict


class _Puzzle(TypedDict):
    target: int
    values: list[int]


class Solution:
    _operators: Iterable[Callable[[int, int], int]]

    def __init__(
        self,
        operators: Iterable[Callable[[int, int], int]],
    ) -> None:
        self._operators = operators

    def calculate_calibration_total(self, puzzles: Iterable[_Puzzle]) -> int:
        total = 0
        for puzzle in puzzles:
            if self._is_possible(puzzle):
                total += puzzle["target"]
        return total

    def _is_possible(self, puzzle: _Puzzle) -> bool:
        target, values = puzzle["target"], puzzle["values"]
        is_possible = False
        combinations = product(self._operators, repeat=len(values) - 1)
        for comb in combinations:
            total = values[0]
            for i, operate in enumerate(comb):
                total = operate(total, values[i + 1])
            if total == target:
                is_possible = True
                break
        return is_possible


class Operator:
    @staticmethod
    def add_operate(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def multiply_operate(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def concatenation_operate(a: int, b: int) -> int:
        digits = floor(log10(b)) + 1
        return a * 10**digits + b
