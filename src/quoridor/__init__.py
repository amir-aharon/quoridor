from .board import Board, BorderState, CellState, Direction, VertexState
from .display import Display
from .player import Player


def simulate_display(size) -> None:
    b = Board(size)
    b.place_wall((0, 0), Direction.H)
    b.place_wall((6, 4), Direction.H)
    b.place_wall((7, 5), Direction.V)
    d = Display(b)
    d.update_display()
