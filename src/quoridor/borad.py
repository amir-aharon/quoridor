from enum import Enum
from typing import List, Tuple


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


class Direction(Enum):
    H = 0
    V = 1


class Board:
    def __init__(self, board_size: int = 9) -> None:
        self.cells: List[List[CellState]] = [[CellState.FREE for col in range(board_size)] for row in range(board_size)]
        self.vertices: List[List[VertexState]] = [
            [VertexState.FREE for col in range(board_size - 1)] for row in range(board_size - 1)
        ]
        self.horizontal_borders: List[List[BorderState]] = [
            [BorderState.FREE for col in range(board_size)] for row in range(board_size - 1)
        ]
        self.vertical_borders: List[List[BorderState]] = [
            [BorderState.FREE for col in range(board_size - 1)] for row in range(board_size)
        ]
        # self.players = [Player((0, board_size // 2)), Player((board_size - 1, board_size // 2))]

    def is_valid_wall(self, loc: Tuple[int, int], direction: Direction) -> bool:
        row, col = loc
        if direction == Direction.H:
            matrix = self.horizontal_borders
            row_limit = len(self.horizontal_borders)
            col_limit = len(self.horizontal_borders[0]) - 1
        elif direction == Direction.V:
            matrix = self.vertical_borders
            row_limit = len(self.vertical_borders) - 1
            col_limit = len(self.vertical_borders[0])

        if row < 0 or row >= row_limit or col < 0 or col >= col_limit:
            return False
        if (
            self.vertices[row][col] != VertexState.FREE
            or matrix[row][col] != BorderState.FREE
            or matrix[row + (direction == Direction.V)][col + (direction == Direction.H)] != BorderState.FREE
        ):
            return False
        return True

    def get_valid_walls(self, direction: Direction) -> List[Tuple[int, int]]:
        possible_placements = []
        for row in range(len(self.vertices)):
            for col in range(len(self.vertices[0])):
                print(row, col)
                loc = (row, col)
                if self.is_valid_wall(loc, direction):
                    possible_placements.append(loc)
        return possible_placements

    def place_wall(self, loc: Tuple[int, int], direction: Direction) -> None:
        row, col = loc
        self.vertices[row][col] = VertexState.OCCUPIED
        if direction == Direction.H:
            self.horizontal_borders[row][col] = BorderState.OCCUPIED
            self.horizontal_borders[row][col + 1] = BorderState.OCCUPIED
        elif direction == Direction.V:
            self.vertical_borders[row][col] = BorderState.OCCUPIED
            self.vertical_borders[row + 1][col] = BorderState.OCCUPIED

    @classmethod
    def validate_board_size(size: int) -> bool:
        return size % 2 == 1  # and size > 5
