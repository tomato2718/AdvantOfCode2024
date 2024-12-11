__all__ = ["TestSolution"]

from src.day10 import Solution
from tests.helper import Testable

TEST_CASE = [
    [8, 9, 0, 1, 0, 1, 2, 3],
    [7, 8, 1, 2, 1, 8, 7, 4],
    [8, 7, 4, 3, 0, 9, 6, 5],
    [9, 6, 5, 4, 9, 8, 7, 4],
    [4, 5, 6, 7, 8, 9, 0, 3],
    [3, 2, 0, 1, 9, 0, 1, 2],
    [0, 1, 3, 2, 9, 8, 0, 1],
    [1, 0, 4, 5, 6, 7, 3, 2],
]


class TestSolution(Testable):
    def test_find_possible_path_count_givenMap_returnCountOfPossiblePath(self) -> None:
        count = Solution.find_possible_path_count(TEST_CASE)

        assert count == 36
