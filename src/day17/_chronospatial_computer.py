__all__ = ["ChronospatialComputer", "Mapper"]

from abc import ABC, abstractmethod
from typing import Sequence, TypedDict


class Registers(TypedDict):
    A: int
    B: int
    C: int


class OperandMapper(ABC):
    @abstractmethod
    def get(self, computer: "ChronospatialComputer", operand: int) -> int:
        pass


class OpcodeExecutor(ABC):
    @abstractmethod
    def execute(
        self, computer: "ChronospatialComputer", opcode: int, operand: int
    ) -> list[int]:
        pass


class ChronospatialComputer:
    registers: Registers
    operand_mapper: OperandMapper
    pointer: int
    _opcode_executor: OpcodeExecutor

    def __init__(
        self,
        registers: Registers,
        operand_mapper: OperandMapper,
        opcode_executor: OpcodeExecutor,
    ) -> None:
        self.registers = registers
        self.operand_mapper = operand_mapper
        self._opcode_executor = opcode_executor
        self.pointer = 0

    def execute(self, programs: Sequence[int]) -> list[int]:
        length = len(programs) - 1
        output = []
        while self.pointer <= length:
            exec_output = self._opcode_executor.execute(
                self, programs[self.pointer], programs[self.pointer + 1]
            )
            output.extend(exec_output)
        return output


class Mapper(OperandMapper):
    def get(self, computer: ChronospatialComputer, operand: int) -> int:
        match operand:
            case 0:
                return operand
            case 1:
                return operand
            case 2:
                return operand
            case 3:
                return operand
            case 4:
                return computer.registers["A"]
            case 5:
                return computer.registers["B"]
            case 6:
                return computer.registers["C"]
            case _:
                raise Exception()


class Executor(OpcodeExecutor):
    def execute(
        self, computer: ChronospatialComputer, opcode: int, operand: int
    ) -> list[int]:
        combo_operand = computer.operand_mapper.get(computer, operand)
        match opcode:
            case 0:
                computer.registers["A"] //= 2**combo_operand
                computer.pointer += 2
                return []
            case 1:
                computer.registers["B"] ^= operand
                computer.pointer += 2
                return []
            case 2:
                computer.registers["B"] = combo_operand % 8
                computer.pointer += 2
                return []
            case 3:
                if computer.registers["A"]:
                    computer.pointer = operand
                else:
                    computer.pointer += 2
                return []
            case 4:
                computer.registers["B"] ^= computer.registers["C"]
                computer.pointer += 2
                return []
            case 5:
                computer.pointer += 2
                return [combo_operand % 8]
            case 6:
                computer.registers["B"] = computer.registers["A"] // (2**combo_operand)
                computer.pointer += 2
                return []
            case 7:
                computer.registers["C"] = computer.registers["A"] // (2**combo_operand)
                computer.pointer += 2
                return []
            case _:
                raise Exception()
