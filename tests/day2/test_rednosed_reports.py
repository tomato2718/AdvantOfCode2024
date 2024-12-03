__all__ = []

from src.day2 import Solution
from tests.helper import Testable

TEST_CASE = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


class TestSolution(Testable):
    def test_count_safe_reports_givenPuzzle_returnCountOfSafeReports(self) -> None:
        solution = Solution()

        assert solution.count_safe_reports(TEST_CASE) == 2
