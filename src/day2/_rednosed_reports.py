_Levels = list[int]
_Puzzle = list[_Levels]


class Solution:

    def __init__(self) -> None:
        ...

    def count_safe_reports(self, puzzle: _Puzzle) -> int:
        safe_reports = 0
        for levels in puzzle:
            if self._is_safe(levels):
                safe_reports += 1
        return safe_reports

    def _is_safe(self, levels: _Levels) -> bool:
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
