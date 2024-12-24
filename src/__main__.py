from . import (
    day1,
    day2,
    day3,
    day4,
    day5,
    day6,
    day7,
    day8,
    day9,
    day10,
    day11,
    day13,
    day14,
    day15,
    day18,
)


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


def solve_day9() -> None:
    print("===== Day9 =====")
    diskmap = day9.parse_input(".puzzle/d9")
    print(day9.Solution.calculate_checksum(diskmap))


def solve_day10() -> None:
    print("===== Day10 =====")
    map_ = day10.parse_input(".puzzle/d10")
    print(day10.Solution.find_possible_path_count(map_))
    print(day10.Solution2.find_possible_path_rating(map_))


def solve_day11() -> None:
    print("===== Day11 =====")
    stones = day11.parse_input(".puzzle/d11")
    solution = day11.Solution(
        day11.Replace0To1(
            day11.SplitEvenDigits(day11.MultiplyBy2024(day11.Unchanged()))
        )
    )
    print(solution.simulate(stones, count=25))
    print(solution.simulate(stones, count=75))


def solve_day13() -> None:
    print("===== Day13 =====")
    puzzles = day13.parse_input(".puzzle/d13")
    print(day13.Solution.find_fewest_token_to_spend(puzzles))
    print(day13.Solution.find_fewest_token_to_spend_with_prize_modified(puzzles))


def solve_day14() -> None:
    print("===== Day14 =====")
    robots = day14.parse_input(".puzzle/d14")
    solution = day14.Solution(robots, (101, 103))
    print(solution.calculate_safety_factor(100))

    from re import compile

    pattern = compile(r".*\.{10,}.*")
    for i in range(10000):
        solution = day14.Solution(robots, (101, 103))
        solution.calculate_safety_factor(i)
        for row in solution.map:
            row_string = "".join(["." if c else " " for c in row])
            if pattern.match(row_string):
                target = i
                break

    solution = day14.Solution(robots, (101, 103))
    solution.calculate_safety_factor(target)
    print(target)
    for row in solution.map:
        row_string = "".join(["." if c else " " for c in row])
        print(row_string)


def solve_day15() -> None:
    print("===== Day15 =====")
    map_, commands = day15.parse_input(".puzzle/d15")
    solution = day15.Solution(map_)
    solution.execute(commands)
    print(solution.get_gps_coordinates())


def solve_day18() -> None:
    print("===== Day18 =====")
    cells = day18.parse_input(".puzzle/d18")
    print(day18.Solution.find_minimum_steps(cells[:1024], size=70))
    print(day18.Solution.find_first_cell_block_exit(cells, size=70))


if __name__ == "__main__":
    solve_day18()
