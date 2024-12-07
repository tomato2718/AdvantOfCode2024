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

    # TODO: Solve it, having no idea yet.
    def skip_test_get_positions_stuck_guard_whenCalled_returnPositionsCanMakeGuardStuckInLoop(
        self,
    ) -> None:
        solution = Solution(MAP)

        result = solution.get_positions_stuck_guard()

        assert result == 6

