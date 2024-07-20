from typing import Tuple

from .board import Board, Direction


class Player:
    def __init__(self, position: Tuple[int, int]):
        self.position = position
        self.walls_left = 10

    def request_place_wall(self, board: Board, position: Tuple[int, int], direction: Direction) -> None:
        if self.walls_left > 0:
            return board.place_wall(self, position, direction)
