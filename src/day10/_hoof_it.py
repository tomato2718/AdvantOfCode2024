__all__ = ["Solution"]

from collections.abc import Sequence

_Height = int
_Map = Sequence[Sequence[_Height]]
_Coordinate = tuple[int, int]
_Heads = set[_Coordinate]
_Score = int


class Solution:
    _map: _Map

    @classmethod
    def find_possible_path_count(cls, __map: _Map) -> int:
        next_start_height, next_end_height = 0, 9
        target_from_start, target_from_end = cls._init_bidirectional_search(__map)

        for _ in range(5):
            next_start_height += 1
            raw_results = [
                cls._check_around(__map, target, heads, next_start_height)
                for target, heads in target_from_start.items()
            ]
            target_from_start = cls._combine_raw_results(raw_results)

        for _ in range(4):
            next_end_height -= 1
            raw_results = [
                cls._check_around(__map, target, heads, next_end_height)
                for target, heads in target_from_end.items()
            ]
            target_from_end = cls._combine_raw_results(raw_results)

        return cls._count_trailheads(target_from_start, target_from_end)

    @staticmethod
    def _init_bidirectional_search(
        __map: _Map,
    ) -> tuple[dict[_Coordinate, _Heads], dict[_Coordinate, _Heads]]:
        start, end = {}, {}
        for y, row in enumerate(__map):
            for x, height in enumerate(row):
                match height:
                    case 0:
                        start[(x, y)] = {(x, y)}
                    case 9:
                        end[(x, y)] = {(x, y)}
        return (start, end)

    @staticmethod
    def _check_around(
        __map: _Map, coordinate: _Coordinate, current_heads: _Heads, height: int
    ) -> dict[_Coordinate, _Heads]:
        accepted_coordinates = {}
        x, y = coordinate
        if x > 0 and __map[y][x - 1] == height:
            accepted_coordinates[(x - 1, y)] = current_heads
        if x < len(__map[0]) - 1 and __map[y][x + 1] == height:
            accepted_coordinates[(x + 1, y)] = current_heads
        if y > 0 and __map[y - 1][x] == height:
            accepted_coordinates[(x, y - 1)] = current_heads
        if y < len(__map) - 1 and __map[y + 1][x] == height:
            accepted_coordinates[(x, y + 1)] = current_heads
        return accepted_coordinates

    @staticmethod
    def _combine_raw_results(
        results: list[dict[_Coordinate, _Heads]],
    ) -> dict[_Coordinate, _Heads]:
        base = results.pop()
        for result in results:
            for coord, heads in result.items():
                if coord in base:
                    base[coord] = base[coord] | heads
                else:
                    base[coord] = heads
        return base

    @staticmethod
    def _count_trailheads(
        start: dict[_Coordinate, _Heads], end: dict[_Coordinate, _Heads]
    ) -> int:
        trailheads = set()
        for coord, heads in start.items():
            for tail in end.get(coord, set()):
                for head in heads:
                    trailheads.add((head, tail))
        return len(trailheads)


class Solution2:
    _map: _Map

    @classmethod
    def find_possible_path_rating(cls, __map: _Map) -> int:
        next_start_height, next_end_height = 0, 9
        target_from_start, target_from_end = cls._init_bidirectional_search(__map)

        for _ in range(5):
            next_start_height += 1
            raw_results = [
                cls._check_around(__map, target, score, next_start_height)
                for target, score in target_from_start.items()
            ]
            target_from_start = cls._combine_raw_results(raw_results)

        for _ in range(4):
            next_end_height -= 1
            raw_results = [
                cls._check_around(__map, target, score, next_end_height)
                for target, score in target_from_end.items()
            ]
            target_from_end = cls._combine_raw_results(raw_results)

        return cls._count_trailheads_rating(target_from_start, target_from_end)

    @staticmethod
    def _init_bidirectional_search(
        __map: _Map,
    ) -> tuple[dict[_Coordinate, _Score], dict[_Coordinate, _Score]]:
        start, end = {}, {}
        for y, row in enumerate(__map):
            for x, height in enumerate(row):
                match height:
                    case 0:
                        start[(x, y)] = 1
                    case 9:
                        end[(x, y)] = 1
        return (start, end)

    @staticmethod
    def _check_around(
        __map: _Map, coordinate: _Coordinate, score: _Score, height: int
    ) -> dict[_Coordinate, _Score]:
        accepted_coordinates = {}
        x, y = coordinate
        if x > 0 and __map[y][x - 1] == height:
            accepted_coordinates[(x - 1, y)] = score
        if x < len(__map[0]) - 1 and __map[y][x + 1] == height:
            accepted_coordinates[(x + 1, y)] = score
        if y > 0 and __map[y - 1][x] == height:
            accepted_coordinates[(x, y - 1)] = score
        if y < len(__map) - 1 and __map[y + 1][x] == height:
            accepted_coordinates[(x, y + 1)] = score
        return accepted_coordinates

    @staticmethod
    def _combine_raw_results(
        results: list[dict[_Coordinate, _Score]],
    ) -> dict[_Coordinate, _Score]:
        base = results.pop()
        for result in results:
            for coord, score in result.items():
                if coord in base:
                    base[coord] += score
                else:
                    base[coord] = score
        return base

    @staticmethod
    def _count_trailheads_rating(
        start: dict[_Coordinate, _Score], end: dict[_Coordinate, _Score]
    ) -> int:
        rating = 0
        for coord, score in start.items():
            rating += score * end.get(coord, 0)
        return rating
