__all__ = ["TestSolution"]

from src.day3 import Solution
from tests.helper import Testable


class TestSolution(Testable):
    def test_add_up_mul_givenNoisedString_returnSumOfMulInIt(self) -> None:
        TEST_CASE = (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
        solution = Solution()

        result = solution.add_up_mul(TEST_CASE)

        assert result == 161
