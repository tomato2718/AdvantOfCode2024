__all__ = ["TestSolution"]

from src.day11 import MultiplyBy2024, Replace0To1, Solution, SplitEvenDigits, Unchanged, Cache
from tests.helper import Testable

TEST_CASE = [125, 17]


class TestSolution(Testable):
    def test_simulate_givenStonesAndTimes_returnCountOfStonesAfterProcess(self) -> None:
        rules = Replace0To1(SplitEvenDigits(MultiplyBy2024(Unchanged())))
        solution = Solution(rules)

        count = solution.simulate(TEST_CASE, count=25)

        assert count == 55312

    def test_simulate_givenStonesAndTimesWithCache_returnCountOfStonesAfterProcess(self) -> None:
        rules = Cache(Replace0To1(SplitEvenDigits(MultiplyBy2024(Unchanged()))))
        solution = Solution(rules)

        count = solution.simulate(TEST_CASE, count=25)

        assert count == 55312