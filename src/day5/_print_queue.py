__all__ = ["Solution"]

from typing import Iterable

_Page = int
_NotAfter = set[_Page]


class Solution:
    _orders: dict[_Page, _NotAfter]

    def __init__(self, orders: Iterable[tuple[_Page, _Page]]) -> None:
        self._orders = self._parse_raw_orders(orders)

    def _parse_raw_orders(
        self, raw_orders: Iterable[tuple[_Page, _Page]]
    ) -> dict[_Page, _NotAfter]:
        orders: dict[_Page, _NotAfter] = {}
        for page, not_after in raw_orders:
            if page not in orders:
                orders[page] = {not_after}
            else:
                orders[page].add(not_after)
        return orders

    def get_correct_updates(self, updates: Iterable[list[_Page]]) -> int:
        total = 0
        for pages in updates:
            if self._is_correct(pages):
                total += self._find_middle(pages)
        return total

    def _is_correct(self, pages: list[_Page]) -> bool:
        seen: set[int] = set()
        for page in pages:
            if len(seen & self._orders.get(page, set())) > 0:
                return False
            seen.add(page)
        return True

    def _find_middle(self, pages: list[_Page]) -> _Page:
        middle = len(pages) // 2
        return pages[middle]

    def get_fixed_incorrect_updates(self, updates: Iterable[list[_Page]]) -> int:
        total = 0
        for pages in updates:
            if not self._is_correct(pages):
                fixed = self._fix_incorrect_pages(pages)
                total += self._find_middle(fixed)
        return total

    def _fix_incorrect_pages(self, pages: list[_Page]) -> list[_Page]:
        weights = {page: 0 for page in pages}
        for page in pages:
            for not_after in self._orders.get(page, set()):
                if not_after in weights:
                    weights[not_after] += 1
        return sorted(pages, key=lambda x: weights[x])
