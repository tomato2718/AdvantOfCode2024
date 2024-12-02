from . import day1
from ._input_parser import parse_input

PUZZLE = ".input.puzzle"

if __name__ == "__main__":
    input = parse_input(PUZZLE)

    solution = day1.Solution(*input)
    print(solution.get_distance())
    print(solution.get_similarity_score())
