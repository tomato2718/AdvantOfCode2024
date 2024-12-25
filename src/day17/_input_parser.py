__all__ = ["parse_input"]

from ._chronospatial_computer import Registers


def parse_input(path: str) -> tuple[Registers, list[int]]:
    with open(path, "r") as file:
        registers = Registers(
            A=int(file.readline().strip("\n")[12:]),
            B=int(file.readline().strip("\n")[12:]),
            C=int(file.readline().strip("\n")[12:]),
        )
        file.readline()
        programs = [int(i) for i in file.readline().strip("\n")[9:].split(",")]

    return registers, programs
