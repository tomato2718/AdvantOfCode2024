__all__ = ["TestChronospatialComputer"]

from src.day17._chronospatial_computer import (
    ChronospatialComputer,
    Executor,
    Mapper,
    Registers,
)
from tests.helper import Testable

REGISTERS: Registers = {
    "A": 729,
    "B": 0,
    "C": 0,
}
PROGRAMS = [0, 1, 5, 4, 3, 0]


class TestChronospatialComputer(Testable):
    def test_execute_givenRegistersAndCommands_returnProceedOutput(self) -> None:
        solution = ChronospatialComputer(
            registers=REGISTERS, operand_mapper=Mapper(), opcode_executor=Executor()
        )

        output = solution.execute(PROGRAMS)

        assert output == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]
