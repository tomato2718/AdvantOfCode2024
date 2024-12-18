__all__ = ["TestSolution"]

from src.day14 import Solution
from src.day14._restroom_redoubt import _Robot
from tests.helper import Testable

TEST_CASE = [
    _Robot({"position": (0, 4), "velocity": (3, -3)}),
    _Robot({"position": (6, 3), "velocity": (-1, -3)}),
    _Robot({"position": (10, 3), "velocity": (-1, 2)}),
    _Robot({"position": (2, 0), "velocity": (2, -1)}),
    _Robot({"position": (0, 0), "velocity": (1, 3)}),
    _Robot({"position": (3, 0), "velocity": (-2, -2)}),
    _Robot({"position": (7, 6), "velocity": (-1, -3)}),
    _Robot({"position": (3, 0), "velocity": (-1, -2)}),
    _Robot({"position": (9, 3), "velocity": (2, 3)}),
    _Robot({"position": (7, 3), "velocity": (-1, 2)}),
    _Robot({"position": (2, 4), "velocity": (2, -3)}),
    _Robot({"position": (9, 5), "velocity": (-3, -3)}),
]


class TestSolution(Testable):
    def test_calculate_safety_factor_givenSecondsAfter_returnTotalSafetyFactor(
        self,
    ) -> None:
        solution = Solution(robots=TEST_CASE, map_size=(11, 7))

        factor = solution.calculate_safety_factor(100)

        assert factor == 12
