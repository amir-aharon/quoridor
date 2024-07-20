from typing import Tuple

from .board import Board, Direction


class Player:
    def __init__(self, position: Tuple[int, int]):
        self.position = position
        self.walls_left = 10
