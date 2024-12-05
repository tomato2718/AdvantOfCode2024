__all__ = ["TestSolution"]

from typing import Literal

from src.day4 import FindXMAS, Solution
from tests.helper import Testable


class TestSolution(Testable):
    def test_givenPuzzle_returnXMASCount(self) -> None:
        TEST_CASE: list[list[Literal["X", "M", "A", "S"]]] = [
            ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
            ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
            ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
            ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
            ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
            ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
            ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
            ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
            ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
            ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
        ]

        solution = Solution(search_policy=FindXMAS())

        assert solution.search(TEST_CASE) == 18
