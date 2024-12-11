__all__ = ["TestSolution"]

from src.day9 import Solution
from tests.helper import Testable

TEST_CASE = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]


class TestSolution(Testable):
    def test_calculate_checksum_givenDiskMap_returnCheckSum(self) -> None:
        assert Solution.calculate_checksum(TEST_CASE) == 1928
