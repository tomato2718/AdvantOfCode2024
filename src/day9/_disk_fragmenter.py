__all__ = ["Solution"]


class Solution:
    @classmethod
    def calculate_checksum(cls, diskmap: list[int]) -> int:
        files = cls._parse_diskmap(diskmap)
        cls._swap_block(files)
        checksum = cls._calculate_checksum(files)
        return checksum

    @staticmethod
    def _parse_diskmap(diskmap: list[int]) -> list[int]:
        result = []
        for i, digit in enumerate(diskmap):
            if i & 1:
                result.extend([-1] * digit)
            else:
                result.extend(i // 2 for _ in range(digit))
        return result

    @staticmethod
    def _swap_block(files: list[int]) -> None:
        left, right = 0, len(files) - 1
        while left < right:
            if files[left] != -1:
                left += 1
                continue
            if files[right] == -1:
                right -= 1
                continue
            files[left], files[right] = files[right], files[left]
            left += 1
            right -= 1

    @staticmethod
    def _calculate_checksum(files: list[int]) -> int:
        total = 0
        for index, file in enumerate(files):
            if file == -1:
                break
            total += index * file
        return total
