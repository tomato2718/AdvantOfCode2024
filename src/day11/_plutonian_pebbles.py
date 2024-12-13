__all__ = [
    "Solution",
    "Unchanged",
    "Replace0To1",
    "SplitEvenDigits",
    "MultiplyBy2024",
    "Cache",
]

from abc import ABC, abstractmethod
from functools import cache


class Solution:
    _rule: "Rule"

    def __init__(self, rule: "Rule") -> None:
        self._rule = rule

    def simulate(self, __stones: list[int], *, count: int) -> int:
        return sum(self._simulate(stone, count) for stone in __stones)

    def _simulate(self, stone: int, left: int) -> int:
        if left:
            return sum(
                self._simulate(i, left - 5) for i in self._iterate_five_times(stone)
            )
        else:
            return 1

    @cache
    def _iterate_five_times(self, stone: int) -> tuple[int, ...]:
        result = (stone,)
        for _ in range(5):
            result = tuple(i for prev in result for i in self._rule.execute(prev))
        return result


class _Rule(ABC):
    @abstractmethod
    def execute(self, stone: int) -> tuple[int, ...]:
        pass


class Unchanged(_Rule):
    def execute(self, stone: int) -> tuple[int, ...]:
        return (stone,)


class Rule(_Rule):
    _next: _Rule

    def __init__(self, __next: _Rule) -> None:
        self._next = __next


class Cache(Rule):
    _cache: dict[int, tuple[int, ...]]

    def __init__(self, __next: _Rule) -> None:
        self._cache = {}
        super().__init__(__next)

    def execute(self, stone: int) -> tuple[int, ...]:
        if stone in self._cache:
            return self._cache[stone]
        else:
            result = self._next.execute(stone)
            self._cache[stone] = result
            return result


class Replace0To1(Rule):
    def execute(self, stone: int) -> tuple[int, ...]:
        if stone == 0:
            return (1,)
        else:
            return self._next.execute(stone)


class SplitEvenDigits(Rule):
    def execute(self, stone: int) -> tuple[int, ...]:
        s = str(stone)
        length = len(s)
        if length & 1:
            return self._next.execute(stone)
        else:
            half = length // 2
            return (int(s[:half]), int(s[half:]))


class MultiplyBy2024(Rule):
    def execute(self, stone: int) -> tuple[int, ...]:
        return (stone * 2024,)
