__all__ = ["Solution"]

from collections.abc import Iterable

_X = int
_Y = int
_C = int
_Equotation = tuple[_X, _Y, _C]


class Solution:
    @classmethod
    def find_fewest_token_to_spend(
        cls, puzzles: Iterable[tuple[_Equotation, _Equotation]]
    ) -> int:
        total = 0
        for puzzle in puzzles:
            a, b = cls.solve_linear_equotation(*puzzle)
            if (a % 1 == 0 and a <= 100) and (b % 1 == 0 and b <= 100):
                total += 3 * int(a) + int(b)
        return total

    @classmethod
    def find_fewest_token_to_spend_with_prize_modified(
        cls, puzzles: Iterable[tuple[_Equotation, _Equotation]]
    ) -> int:
        FACTOR = 10000000000000
        modified_puzzles = [
            (
                (e1[0], e1[1], e1[2] + FACTOR),
                (e2[0], e2[1], e2[2] + FACTOR),
            )
            for e1, e2 in puzzles
        ]
        total = 0
        for puzzle in modified_puzzles:
            a, b = cls.solve_linear_equotation(*puzzle)
            if a % 1 == 0 and b % 1 == 0:
                total += 3 * int(a) + int(b)
        return total

    @staticmethod
    def solve_linear_equotation(
        e1: _Equotation, e2: _Equotation
    ) -> tuple[float, float]:
        a = (e1[2] * e2[1] - e1[1] * e2[2]) / (e1[0] * e2[1] - e1[1] * e2[0])
        b = (e1[2] - e1[0] * a) / e1[1]
        return (a, b)
