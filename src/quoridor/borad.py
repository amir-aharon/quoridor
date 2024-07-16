from enum import Enum
from typing import List


class CellState(Enum):
    FREE = 0
    A = 1
    B = 2


class VertexState(Enum):
    FREE = 0
    OCCUPIED = 1


class BorderState(Enum):
    FREE = 0
    OCCUPIED = 1


"""
9x9 cells
8*9 vertical walls
9*8 horizontal walls
8*8 vertex
"""


class Board:
    @classmethod
    def validate_board_size(size: int) -> bool:
        return size % 2 == 1 and size > 5

    def __init__(self, board_size: int = 9) -> None:
        self.cells: List[List[CellState]] = [
            [CellState.FREE for col in range(board_size)]
            for row in range(board_size)
        ]
        self.vertices: List[List[VertexState]] = [
            [VertexState.FREE for col in range(board_size - 1)]
            for row in range(board_size - 1)
        ]
        self.horizontal_borders: List[List[BorderState]] = [
            [BorderState.FREE for col in range(board_size)]
            for row in range(board_size - 1)
        ]
        self.vertical_borders: List[List[BorderState]] = [
            [BorderState.FREE for col in range(board_size - 1)]
            for row in range(board_size)
        ]
