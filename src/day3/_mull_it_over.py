__all__ = ["Solution"]

from re import findall


class Solution:
    def add_up_mul(self, noised_string: str) -> int:
        muls = findall(r"mul\(\d+,\d+\)", noised_string)
        sum_ = 0
        for mul in muls:
            a, b = findall(r"\d+", mul)
            sum_ += int(a) * int(b)
        return sum_
