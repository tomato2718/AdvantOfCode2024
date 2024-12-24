__all__ = ["TestSolution", "TestPriorityQueue", "TestCoordinate", "TestAStar"]

from src.day18._ram_run import AStar, Coordinate, PriorityQueue, Solution, _Map
from tests.helper import Testable

TEST_CASE = [
    (5, 4),
    (4, 2),
    (4, 5),
    (3, 0),
    (2, 1),
    (6, 3),
    (2, 4),
    (1, 5),
    (0, 6),
    (3, 3),
    (2, 6),
    (5, 1),
    (1, 2),
    (5, 5),
    (2, 5),
    (6, 5),
    (1, 4),
    (0, 4),
    (6, 4),
    (1, 1),
    (6, 1),
    (1, 0),
    (0, 5),
    (1, 6),
    (2, 0),
]


class TestSolution(Testable):
    def test_find_minimum_steps_givenCorrupptedCells_returnLengthOfShortestPathFromLeftTopToRightBottom(
        self,
    ) -> None:
        steps = Solution.find_minimum_steps(TEST_CASE[:12], size=6)

        assert steps == 22

    def test_find_first_cell_block_exit_givenCorrupptedCells_returnTheCellBlockThePathToExit(
        self,
    ) -> None:
        cell = Solution.find_first_cell_block_exit(TEST_CASE, size=6)

        assert cell == (6, 1)


class TestAStar(Testable):
    def test_simulate_whenCalled_returnLengthOfShortestPathFromStartToEnd(
        self,
    ) -> None:
        TEST_CASE: _Map = [
            [".", ".", ".", "#", ".", ".", "."],
            [".", ".", "#", ".", ".", "#", "."],
            [".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", "#", ".", ".", "#"],
            [".", ".", "#", ".", ".", "#", "."],
            [".", "#", ".", ".", "#", ".", "."],
            ["#", ".", "#", ".", ".", ".", "."],
        ]
        a_star = AStar(
            TEST_CASE,
            start=Coordinate(0, 0),
            end=Coordinate(len(TEST_CASE) - 1, len(TEST_CASE[0]) - 1),
        )

        length = a_star.simulate()

        assert length == 22


class TestPriorityQueue(Testable):
    def test_is_empty_whenCalled_returnIfQueueIsEmpty(self) -> None:
        queue = PriorityQueue()

        assert queue.is_empty() is True

    def test_push_givenCoordinate_pushItIntoHeap(self) -> None:
        queue = PriorityQueue()

        TARGET = Coordinate(0, 0)
        SCORE = 0

        queue.push(TARGET, SCORE)

        assert (SCORE, id(TARGET), TARGET) in queue._heap

    def test_pop_whenCalled_returnCoordinateWithLowestCost(self) -> None:
        queue = PriorityQueue()

        TARGET = Coordinate(0, 0)

        queue.push(TARGET, 0)
        queue.push(Coordinate(1, 2), 10)
        queue.push(Coordinate(3, 4), 15)

        assert queue.pop() == TARGET


class TestCoordinate(Testable):
    def test_distance_givenAnotherCoordinate_returnDistanceOfCoordinates(
        self,
    ) -> None:
        a = Coordinate(0, 0)
        b = Coordinate(3, 4)

        distance = a.distance_to(b)

        assert distance == 7
