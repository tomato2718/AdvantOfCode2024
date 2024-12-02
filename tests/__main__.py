from . import day1


def main() -> None:
    for test_name in day1.__all__:
        test_func = getattr(day1, test_name)
        test_func()


if __name__ == "__main__":
    main()
