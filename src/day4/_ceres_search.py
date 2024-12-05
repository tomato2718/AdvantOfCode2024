__all__ = ["Solution", "FindXMAS", "FindX_MAS"]

from typing import Callable, Literal

_XmasChar = Literal["X", "M", "A", "S"]
_Puzzle = list[list[_XmasChar]]
_Index = tuple[int, int]
_SearchPolicy = Callable[[_Puzzle, _Index], int]


class Solution:
    _search_policy: _SearchPolicy

    def __init__(self, *, search_policy: _SearchPolicy) -> None:
        self._search_policy = search_policy

    def search(self, puzzle: list[list[_XmasChar]]) -> int:
        xmas_count = 0
        for y, chars in enumerate(puzzle):
            for x in range(len(chars)):
                xmas_count += self._search_policy(puzzle, (x, y))
        return xmas_count


class FindXMAS:
    _puzzle: _Puzzle

    def __call__(self, puzzle: _Puzzle, index: _Index) -> int:
        self._puzzle = puzzle
        x, y = index
        match puzzle[y][x]:
            case "X":
                count = self._check(x, y, "XMAS")
            case "S":
                count = self._check(x, y, "SAMX")
            case _:
                count = 0
        return count

    def _check(self, x: int, y: int, want: str) -> int:
        return (
            self._check_horizontal(x, y, want)
            + self._check_diagonal(x, y, want)
            + self._check_vertical(x, y, want)
            + self._check_reversed_diagonal(x, y, want)
        )

    def _check_horizontal(self, x: int, y: int, want: str) -> bool:
        try:
            return (
                self._puzzle[y][x] == want[0]
                and self._puzzle[y][x + 1] == want[1]
                and self._puzzle[y][x + 2] == want[2]
                and self._puzzle[y][x + 3] == want[3]
            )
        except IndexError:
            return False

    def _check_vertical(self, x: int, y: int, want: str) -> bool:
        try:
            return (
                self._puzzle[y][x] == want[0]
                and self._puzzle[y + 1][x] == want[1]
                and self._puzzle[y + 2][x] == want[2]
                and self._puzzle[y + 3][x] == want[3]
            )
        except IndexError:
            return False

    def _check_diagonal(self, x: int, y: int, want: str) -> bool:
        try:
            return (
                self._puzzle[y][x] == want[0]
                and self._puzzle[y + 1][x + 1] == want[1]
                and self._puzzle[y + 2][x + 2] == want[2]
                and self._puzzle[y + 3][x + 3] == want[3]
            )
        except IndexError:
            return False

    def _check_reversed_diagonal(self, x: int, y: int, want: str) -> bool:
        try:
            if x >= 3:
                return (
                    self._puzzle[y][x] == want[0]
                    and self._puzzle[y + 1][x - 1] == want[1]
                    and self._puzzle[y + 2][x - 2] == want[2]
                    and self._puzzle[y + 3][x - 3] == want[3]
                )
            else:
                return False
        except IndexError:
            return False


class FindX_MAS:
    def __call__(self, puzzle: _Puzzle, index: _Index) -> int:
        x, y = index
        if x == 0 or y == 0 or puzzle[y][x] != "A":
            return 0
        try:
            return self._is_mas(
                (puzzle[y + 1][x - 1], puzzle[y][x], puzzle[y - 1][x + 1])
            ) and self._is_mas(
                (puzzle[y - 1][x - 1], puzzle[y][x], puzzle[y + 1][x + 1])
            )
        except IndexError:
            return 0

    def _is_mas(self, t: tuple[_XmasChar, _XmasChar, _XmasChar]) -> bool:
        return t == ("M", "A", "S") or t == ("S", "A", "M")
