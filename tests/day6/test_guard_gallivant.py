__all__ = ["TestSolution"]


from src.day6 import Solution
from src.day6._guard_gallivant import _Map
from tests.helper import Testable

MAP: _Map = [
    [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
]


class TestSolution(Testable):
    def test_get_visited_positions_whenCalled_returnDistinctPositionsTheGuardVisit(
        self,
    ) -> None:
        solution = Solution(MAP)

        result = solution.get_visited_positions()

        assert result == 41
