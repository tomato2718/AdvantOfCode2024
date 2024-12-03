__all__ = ["TestSolution", "TestValidator"]

from src.day2 import Solution, Validator
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
        solution = Solution(validator_function=Validator.validate)

        assert solution.count_safe_reports(TEST_CASE) == 2

    def test_count_safe_reports_givenPuzzleWithTolerateOnce_returnCountOfSafeReports(
        self,
    ) -> None:
        solution = Solution(validator_function=Validator.tolerated_validate)

        assert solution.count_safe_reports(TEST_CASE) == 4


class TestValidator(Testable):
    def test_validate_givenLevels_returnIsSafe(self) -> None:
        TEST_CASE = [
            ([7, 6, 4, 2, 1], True),
            ([1, 2, 7, 8, 9], False),
            ([9, 7, 6, 2, 1], False),
            ([1, 3, 2, 4, 5], False),
            ([8, 6, 4, 4, 1], False),
            ([1, 3, 6, 7, 9], True),
        ]

        assert all(
            Validator.validate(test_case) == expect for test_case, expect in TEST_CASE
        )

    def test_tolerated_validate_givenLevelsWithBadLevelsLessThanOnce_returnTrue(
        self,
    ) -> None:
        LEVELS = (
            [3, 4, 5, 6, 2],
            [3, 4, 3, 2, 1],
        )

        assert all(Validator.tolerated_validate(level) for level in LEVELS)

    def test_givenLevelsWithBadLevelsMoreThanOnce_returnFalse(self) -> None:
        LEVELS = [1, 2, 7, 8, 9]

        assert Validator.tolerated_validate(LEVELS) is False
