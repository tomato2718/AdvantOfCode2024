from . import day1, day2, day3, day4, day5, day6, day7, day8


def solve_day1() -> None:
    print("===== Day1 =====")
    input = day1.parse_input(".puzzle/d1")
    solution = day1.Solution(*input)
    print(solution.get_distance())
    print(solution.get_similarity_score())


def solve_day2() -> None:
    print("===== Day2 =====")
    input = day2.parse_input(".puzzle/d2")
    solution = day2.Solution(validator_function=day2.Validator.validate)
    print(solution.count_safe_reports(input))
    solution = day2.Solution(validator_function=day2.Validator.tolerated_validate)
    print(solution.count_safe_reports(input))


def solve_day3() -> None:
    print("===== Day3 =====")
    input = day3.parse_input(".puzzle/d3")
    solution = day3.Solution()
    print(solution.add_up_mul(input))
    print(solution.add_up_mul_with_switch(input))


def solve_day4() -> None:
    print("===== Day4 =====")
    input = day4.parse_input(".puzzle/d4")
    solution = day4.Solution(search_policy=day4.FindXMAS())
    print(solution.search(input))
    solution = day4.Solution(search_policy=day4.FindX_MAS())
    print(solution.search(input))


def solve_day5() -> None:
    print("===== Day5 =====")
    orders, updates = day5.parse_input(".puzzle/d5")
    solution = day5.Solution(orders)
    print(solution.get_correct_updates(updates))
    print(solution.get_fixed_incorrect_updates(updates))


def solve_day6() -> None:
    print("===== Day6 =====")
    map_ = day6.parse_input(".puzzle/d6")
    solution = day6.Solution(map_)
    print(solution.get_visited_positions())


def solve_day7() -> None:
    print("===== Day7 =====")
    puzzles = day7.parse_input(".puzzle/d7")
    solution = day7.Solution(
        operators=[
            day7.Operator.add_operate,
            day7.Operator.multiply_operate,
        ]
    )
    print(solution.calculate_calibration_total(puzzles))
    solution = day7.Solution(
        operators=[
            day7.Operator.add_operate,
            day7.Operator.multiply_operate,
            day7.Operator.concatenation_operate,
        ]
    )
    print(solution.calculate_calibration_total(puzzles))


def solve_day8() -> None:
    print("===== Day8 =====")
    map_ = day8.parse_input(".puzzle/d8")
    solution = day8.Solution(map_)
    print(solution.count_closest_antinodes())
    print(solution.count_all_antinodes())


if __name__ == "__main__":
    solve_day1()
    solve_day2()
    solve_day3()
    solve_day4()
    solve_day5()
    solve_day6()
    solve_day7()
    solve_day8()
