from . import day1, day2
from ._input_parser import parse_day1_input, parse_day2_input

if __name__ == "__main__":
    input = parse_day1_input(".input.puzzle.day1")

    solution = day1.Solution(*input)
    print(solution.get_distance())
    print(solution.get_similarity_score())

    input = parse_day2_input(".input.puzzle.day2")
    solution = day2.Solution(validator_function=day2.Validator.validate)
    print(solution.count_safe_reports(input))
    solution = day2.Solution(validator_function=day2.Validator.tolerated_validate)
    print(solution.count_safe_reports(input))
