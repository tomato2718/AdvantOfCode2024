__all__ = ["TestSolution"]

from src.day7 import Operator, Solution
from src.day7._bridge_repair import _Puzzle
from tests.helper import Testable

TEST_CASE: list[_Puzzle] = [
    {"target": 190, "values": [10, 19]},
    {"target": 3267, "values": [81, 40, 27]},
    {"target": 83, "values": [17, 5]},
    {"target": 156, "values": [15, 6]},
    {"target": 7290, "values": [6, 8, 6, 15]},
    {"target": 161011, "values": [16, 10, 13]},
    {"target": 192, "values": [17, 8, 14]},
    {"target": 21037, "values": [9, 7, 18, 13]},
    {"target": 292, "values": [11, 6, 16, 20]},
]


class TestSolution(Testable):
    def test_calculate_calibration_total_withAddAndMultiplyOperator_returnCalibratedTotal(
        self,
    ) -> None:
        solution = Solution(
            operators=[
                Operator.add_operate,
                Operator.multiply_operate,
            ]
        )

        result = solution.calculate_calibration_total(TEST_CASE)

        assert result == 3749

    def test_calculate_calibration_total_withAddMultiplyAndConcatenationOperator_returnCalibratedTotal(
        self,
    ) -> None:
        solution = Solution(
            operators=[
                Operator.add_operate,
                Operator.multiply_operate,
                Operator.concatenation_operate,
            ]
        )

        result = solution.calculate_calibration_total(TEST_CASE)

        assert result == 11387
