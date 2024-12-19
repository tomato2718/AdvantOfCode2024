__all__ = ["Solution"]

from collections.abc import Iterable
from typing import Literal, Sequence

_Robot = Literal["@"]
_Box = Literal["O"]
_Wall = Literal["#"]
_Space = Literal["."]
_Cell = _Robot | _Box | _Wall | _Space
_Map = Sequence[Sequence[_Cell]]
_Move = Literal["^", ">", "v", "<"]


class Solution:
    _sokoban: "Sokoban"

    def __init__(self, _map: _Map) -> None:
        self._sokoban = Sokoban(_map)

    def execute(self, commands: Iterable[_Move]) -> None:
        for command in commands:
            match command:
                case "^":
                    self._sokoban.move_up()
                case ">":
                    self._sokoban.move_right()
                case "v":
                    self._sokoban.move_down()
                case "<":
                    self._sokoban.move_left()

    def print_map(self) -> None:
        for row in self._sokoban.map_:
            print(row)

    def get_map(self) -> _Map:
        return self._sokoban.map_

    def get_gps_coordinates(self) -> int:
        total = 0
        for row_index, row in enumerate(self._sokoban.map_):
            for col_index, cell in enumerate(row):
                if cell == "O":
                    total += col_index + row_index * 100
        return total


class Sokoban:
    map_: list[list[_Cell]]
    _player: tuple[int, int]

    def __init__(self, _map: _Map) -> None:
        self.map_ = [[cell for cell in row] for row in _map]
        self._player = self._find_player()

    def _find_player(self) -> tuple[int, int]:
        for row_index, row in enumerate(self.map_):
            for col_index, cell in enumerate(row):
                if cell == "@":
                    return (row_index, col_index)
        raise Exception("Invalid Map")

    def move_up(self) -> None:
        next_row, next_col = self._player[0] - 1, self._player[1]
        box_to_move = 0
        while self.map_[next_row][next_col] == "O":
            box_to_move += 1
            next_row -= 1

        if self.map_[next_row][next_col] == ".":
            self.map_[self._player[0]][self._player[1]] = "."
            self.map_[self._player[0] - 1][self._player[1]] = "@"
            if box_to_move:
                self.map_[self._player[0] - box_to_move - 1][self._player[1]] = "O"
            self._player = self._player[0] - 1, self._player[1]

    def move_right(self) -> None:
        next_row, next_col = self._player[0], self._player[1] + 1
        box_to_move = 0
        while self.map_[next_row][next_col] == "O":
            box_to_move += 1
            next_col += 1

        if self.map_[next_row][next_col] == ".":
            self.map_[self._player[0]][self._player[1]] = "."
            self.map_[self._player[0]][self._player[1] + 1] = "@"
            if box_to_move:
                self.map_[self._player[0]][self._player[1] + box_to_move + 1] = "O"
            self._player = self._player[0], self._player[1] + 1

    def move_down(self) -> None:
        next_row, next_col = self._player[0] + 1, self._player[1]
        box_to_move = 0
        while self.map_[next_row][next_col] == "O":
            box_to_move += 1
            next_row += 1

        if self.map_[next_row][next_col] == ".":
            self.map_[self._player[0]][self._player[1]] = "."
            self.map_[self._player[0] + 1][self._player[1]] = "@"
            if box_to_move:
                self.map_[self._player[0] + box_to_move + 1][self._player[1]] = "O"
            self._player = self._player[0] + 1, self._player[1]

    def move_left(self) -> None:
        next_row, next_col = self._player[0], self._player[1] - 1
        box_to_move = 0
        while self.map_[next_row][next_col] == "O":
            box_to_move += 1
            next_col -= 1

        if self.map_[next_row][next_col] == ".":
            self.map_[self._player[0]][self._player[1]] = "."
            self.map_[self._player[0]][self._player[1] - 1] = "@"
            if box_to_move:
                self.map_[self._player[0]][self._player[1] - box_to_move - 1] = "O"
            self._player = self._player[0], self._player[1] - 1
