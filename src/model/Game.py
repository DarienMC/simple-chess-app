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
    current_position = Position()
    moves = None

    def __init__(self, players):
        self.players = players
