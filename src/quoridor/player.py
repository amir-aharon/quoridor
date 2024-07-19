from typing import Tuple

from .borad import Board, Direction


class Player:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos
        self.walls_left = 10

    def request_place_wall(self, board: Board, pos: Tuple[int, int], direction: Direction) -> None:
        if self.walls_left > 0:
            return board.place_wall(self, pos, direction)
