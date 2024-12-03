from . import day1
from .helper import Testable


def main() -> None:
    for test_name in day1.__all__:
        test_class: type[Testable] = getattr(day1, test_name)
        test_class().run_tests()


if __name__ == "__main__":
    main()
