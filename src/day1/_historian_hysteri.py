__all__ = ["Solution"]


class Solution:
    __lst1: list[int]
    __lst2: list[int]

    def __init__(self, lst1: list[int], lst2: list[int]) -> None:
        self.__lst1 = sorted(lst1)
        self.__lst2 = sorted(lst2)

    def get_distance(self) -> int:
        dist = 0
        for i in range(len(self.__lst1)):
            dist += abs(self.__lst2[i] - self.__lst1[i])
        return dist

    def get_similarity_score(self) -> int:
        counter = self._count_appears(self.__lst2)
        score = 0
        for i in self.__lst1:
            score += i * counter.get(i, 0)
        return score

    def _count_appears(self, lst: list[int]) -> dict[int, int]:
        appears = {}
        for element in lst:
            if element not in appears:
                appears[element] = 1
            else:
                appears[element] += 1
        return appears
