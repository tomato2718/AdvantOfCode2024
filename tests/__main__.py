from . import day1, day2, day3, day4
from .helper import Testable


def main() -> None:
    for day in (day1, day2, day3, day4):
        for test_name in day.__all__:
            test_class: type[Testable] = getattr(day, test_name)
            test_class().run_tests()


if __name__ == "__main__":
    main()
