__all__ = ["Testable"]

from types import FunctionType
from typing import Any, Callable, Self


class Testable:
    def run_tests(self) -> None:
        for name, attribute in self.__class__.__dict__.items():
            if self._is_testable_function(name, attribute):
                self._run_test_function(attribute)

    def _is_testable_function(self, name: str, attribute: Any) -> bool:
        return name.startswith("test_") and isinstance(attribute, FunctionType)

    def _run_test_function(self, test_function: Callable[[Self], None]) -> None:
        test_function(self)
