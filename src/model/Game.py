from enum import Enum
import Position, Move
import numpy as np

class GameState(Enum):
    IN_PROGRESS = 1
    WHITE_WINS = 2
    BLACK_WINS = 3
    DRAW = 4

class Game:
    state = GameState.IN_PROGRESS
    current_position = Position( np., 0)
    moves = None

    def __init__(self, players):
        pass
