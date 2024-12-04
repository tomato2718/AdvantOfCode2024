__all__ = ["Solution"]

from re import findall


class Solution:
    def add_up_mul(self, noised_string: str) -> int:
        muls = findall(r"mul\(\d+,\d+\)", noised_string)
        sum_ = 0
        for mul in muls:
            sum_ += self._parse_mul(mul)
        return sum_

    def _parse_mul(self, mul_string: str) -> int:
        a, b = findall(r"\d+", mul_string)
        return int(a) * int(b)

    def add_up_mul_with_switch(self, noised_string: str) -> int:
        operations: list[str] = findall(
            r"mul\(\d+,\d+\)|do\(\)|don't\(\)", noised_string
        )
        sum_ = 0
        ignoring = False
        for operation in operations:
            if operation.startswith("mul") and not ignoring:
                sum_ += self._parse_mul(operation)
            elif operation == "do()":
                ignoring = False
            elif operation == "don't()":
                ignoring = True
        return sum_
