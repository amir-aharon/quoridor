import pygame

from .board import Board, BorderState, VertexState
from .player import Player


class Display:
    def __init__(self, board: Board):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 900))
        self.board = board
        self.cell_size = 65
        self.margin = 10
        self.colors = {
            "background": (151, 97, 92),
            "grid": (73, 74, 88),
            "player1": (210, 105, 124),
            "player2": (239, 172, 75),
            "wall": (255, 255, 255),
        }
        self.players = [Player((0, self.board.size // 2)), Player((self.board.size - 1, self.board.size // 2))]
        self.board_size = self.board.size * self.cell_size + (self.board.size - 1) * self.margin
        self.offset_x = (self.screen.get_width() - self.board_size) // 2
        self.offset_y = (self.screen.get_height() - self.board_size) // 2

    def draw_board(self):
        self.screen.fill(self.colors["background"])
        for row in range(self.board.size):
            for col in range(self.board.size):
                rect = pygame.Rect(
                    self.offset_x + col * (self.cell_size + self.margin),
                    self.offset_y + row * (self.cell_size + self.margin),
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, self.colors["grid"], rect)
                pygame.draw.rect(self.screen, self.colors["grid"], rect, 1)  # Border

    def draw_players(self):
        for i, player in enumerate(self.players):
            color = self.colors["player1"] if i == 0 else self.colors["player2"]
            pygame.draw.circle(
                self.screen,
                color,
                (
                    self.offset_x + player.position[1] * (self.cell_size + self.margin) + self.cell_size // 2,
                    self.offset_y + player.position[0] * (self.cell_size + self.margin) + self.cell_size // 2,
                ),
                self.cell_size // 2 - self.margin,
            )

    def draw_walls(self):
        for row in range(self.board.size - 1):
            for col in range(self.board.size):
                if self.board.horizontal_borders[row][col] == BorderState.OCCUPIED:
                    pygame.draw.rect(
                        self.screen,
                        self.colors["wall"],
                        (
                            self.offset_x + col * (self.cell_size + self.margin),
                            self.offset_y + row * (self.cell_size + self.margin) + self.cell_size,
                            self.cell_size,
                            self.margin,
                        ),
                    )
        for row in range(self.board.size):
            for col in range(self.board.size - 1):
                if self.board.vertical_borders[row][col] == BorderState.OCCUPIED:
                    print(row, col)
                    pygame.draw.rect(
                        self.screen,
                        self.colors["wall"],
                        (
                            self.offset_x + col * (self.cell_size + self.margin) + self.cell_size,
                            self.offset_y + row * (self.cell_size + self.margin),
                            self.margin,
                            self.cell_size,
                        ),
                    )

    def draw_vertices(self):
        for row in range(self.board.size - 1):
            for col in range(self.board.size - 1):
                if self.board.vertices[row][col] == VertexState.OCCUPIED:
                    pygame.draw.rect(
                        self.screen,
                        self.colors["wall"],
                        (
                            self.offset_x + col * (self.cell_size + self.margin) + self.cell_size,
                            self.offset_y + row * (self.cell_size + self.margin) + self.cell_size,
                            self.margin,
                            self.margin,
                        ),
                    )

    def update_display(self):
        self.draw_board()
        self.draw_players()
        self.draw_walls()
        self.draw_vertices()
        pygame.display.flip()
