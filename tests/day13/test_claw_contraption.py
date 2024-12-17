__all__ = ["TestSolution"]

from src.day13 import Solution
from tests.helper import Testable

PUZZLES = [
    ((94, 22, 8400), (34, 67, 5400)),
    ((26, 67, 12748), (66, 21, 12176)),
    ((17, 84, 7870), (86, 37, 6450)),
    ((69, 27, 18641), (23, 71, 10279)),
]


class TestSolution(Testable):
    def test_find_fewest_token_to_spend_givenPuzzles_returnFewestTokenToSpend(
        self,
    ) -> None:
        assert Solution.find_fewest_token_to_spend(PUZZLES) == 480

    def test_solve_linear_equotation_givenLinearSystem_returnXandY(self) -> None:
        f1 = (94, 22, 8400)
        f2 = (34, 67, 5400)

        assert Solution.solve_linear_equotation(f1, f2) == (80, 40)
