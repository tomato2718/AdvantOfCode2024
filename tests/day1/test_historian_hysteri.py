__all__ = ["TestSolution"]

from src.day1 import Solution
from tests.helper import Testable

TEST_CASE = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


class TestSolution(Testable):
    def test_get_distance_givenTwoList_returnTotalDistanceOfSortedLists(self) -> None:
        solution = Solution(*TEST_CASE)

        assert solution.get_distance() == 11

    def test_get_similarity_score_givenTwoList_returnSimilatiryScoreOfLists(
        self,
    ) -> None:
        solution = Solution(*TEST_CASE)

        assert solution.get_similarity_score() == 31
