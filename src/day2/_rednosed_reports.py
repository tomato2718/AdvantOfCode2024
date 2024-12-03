__all__ = ["Solution", "Validator"]

from typing import Callable

_Levels = list[int]
_Puzzle = list[_Levels]


class Solution:
    _validator_function: Callable[[_Levels], bool]

    def __init__(self, validator_function: Callable[[_Levels], bool]) -> None:
        self._validator_function = validator_function

    def count_safe_reports(self, puzzle: _Puzzle) -> int:
        safe_reports = 0
        for levels in puzzle:
            is_valid = self._validator_function(levels)
            if is_valid:
                safe_reports += 1
        return safe_reports


class Validator:
    @staticmethod
    def validate(levels: _Levels) -> bool:
        if len(levels) <= 1:
            return True

        is_increasing = levels[-1] > levels[0]

        if is_increasing:
            is_safe = all(
                (1 <= (levels[i] - levels[i - 1]) <= 3) for i in range(1, len(levels))
            )
        else:
            is_safe = all(
                (1 <= (levels[i - 1] - levels[i]) <= 3) for i in range(1, len(levels))
            )
        return is_safe

    @classmethod
    def tolerated_validate(cls, levels: _Levels) -> bool:
        return any(
            cls.validate(levels[: i - 1] + levels[i:]) for i in range(len(levels)+1)
        )
