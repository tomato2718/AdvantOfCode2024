from . import day1, day2, day3


def solve_day1() -> None:
    print("===== Day1 =====")
    input = day1.parse_input(".input.puzzle.day1")
    solution = day1.Solution(*input)
    print(solution.get_distance())
    print(solution.get_similarity_score())


def solve_day2() -> None:
    print("===== Day2 =====")
    input = day2.parse_input(".input.puzzle.day2")
    solution = day2.Solution(validator_function=day2.Validator.validate)
    print(solution.count_safe_reports(input))
    solution = day2.Solution(validator_function=day2.Validator.tolerated_validate)
    print(solution.count_safe_reports(input))


def solve_day3() -> None:
    print("===== Day3 =====")
    input = day3.parse_input(".input.puzzle.day3")
    solution = day3.Solution()
    print(solution.add_up_mul(input))
    print(solution.add_up_mul_with_switch(input))


if __name__ == "__main__":
    solve_day1()
    solve_day2()
    solve_day3()
