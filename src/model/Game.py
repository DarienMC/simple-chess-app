from enum import Enum
import Position, Move, Player
import numpy as np

class GameState(Enum):
    IN_PROGRESS = 1
    WHITE_WINS = 2
    BLACK_WINS = 3
    DRAW = 4

class Game:
    state = GameState.IN_PROGRESS
    current_position = Position
    moves = None

    def change_to_subsequent_position(self, move):
        pass

    def play(self):
        while self.state is GameState.IN_PROGRESS:
            if self.current_position.legal_moves is not None:
                move = input(f'{players[current_position.turn_index]} to move: ')
                self.change_to_subsequent_position(move)
            else:
                if self.current_position.in_check:
                    if self.current_position.turn_index is 0:
                        self.state = GameState.WHITE_WINS
                    else:
                        self.state = GameState.BLACK_WINS
                else:
                    self.state = GameState.DRAW

    def __init__(self, players):
        self.players = players
