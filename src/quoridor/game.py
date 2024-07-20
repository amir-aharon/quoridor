import pygame

from .display import Display
from .board import Board, Direction
from .player import Player

PLAYER_MOVEMENTS = {
    pygame.K_h: (0, -1),
    pygame.K_l: (0, 1),
    pygame.K_k: (-1, 0),
    pygame.K_j: (1, 0),
}


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.board.place_wall((0, 3), Direction.V)
        self.board.place_wall((2, 3), Direction.V)
        self.board.place_wall((3, 4), Direction.H)
        self.players = [Player((0, self.board.size // 2)), Player((self.board.size - 1, self.board.size // 2))]
        self.current_player_index = 0
        self.display = Display(self.board, self.players)
        self.running = True
        self.current_possible_player_moves = self.get_possible_player_moves()

    def handle_input(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in self.current_possible_player_moves.keys():
                self.move_player(PLAYER_MOVEMENTS[event.key])

    def get_possible_player_moves(self):
        player = self.players[self.current_player_index]
        possible_moves = []
        for key, direction in PLAYER_MOVEMENTS.items():
            new_position = (player.position[0] + direction[0], player.position[1] + direction[1])
            if self.board.is_valid_move(player.position, new_position):
                possible_moves.append(key)
        return {key: PLAYER_MOVEMENTS[key] for key in possible_moves}

    def move_player(self, direction):

        player = self.players[self.current_player_index]
        new_position = (player.position[0] + direction[0], player.position[1] + direction[1])
        # if self.board.is_valid_move(player, new_position):
        player.position = new_position
        self.current_possible_player_moves = self.get_possible_player_moves()

        # self.check_winner()

    # def place_wall(self):
    #     player = self.players[self.current_player_index]
    #     if self.board.can_place_wall(player):
    #         wall_position = self.get_wall_position()
    #         if wall_position:
    #             self.board.place_wall(wall_position)
    #             self.switch_player()

    # def get_wall_position(self):
    #     # Placeholder for wall placement logic
    #     # Return (row, col, orientation)
    #     return None  # Modify based on actual implementation

    # def check_winner(self):
    #     for player in self.players:
    #         if self.board.has_reached_goal(player):
    #             self.running = False
    #             print(f"{player.name} wins!")

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_input(event)
            self.display.update_display(
                self.players[self.current_player_index], self.current_possible_player_moves.values()
            )
            pygame.time.delay(100)  # Delay for smoother gameplay
