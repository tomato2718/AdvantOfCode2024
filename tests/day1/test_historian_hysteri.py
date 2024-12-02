__all__ = [
    "test_get_distance_givenTwoList_returnTotalDistanceOfSortedLists",
    "test_get_similarity_score_givenTwoList_returnSimilatiryScoreOfLists",
]

from src.day1 import Solution

TEST_CASE = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


def test_get_distance_givenTwoList_returnTotalDistanceOfSortedLists() -> None:
    solution = Solution(*TEST_CASE)

    assert solution.get_distance() == 11


def test_get_similarity_score_givenTwoList_returnSimilatiryScoreOfLists() -> None:
    solution = Solution(*TEST_CASE)

    assert solution.get_similarity_score() == 31
