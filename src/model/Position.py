import numpy as np
import Piece, Move

class Position:
    ''
    # Class attributes
    columns = 8
    rows = 8
    in_check = False
    legal_moves = None

    def calculate_legal_moves(self, pieces, turn_index):
        pass


    # Constructor
    def __init__(self):
        self.pieces = np.array(None).reshape(self.columns,self.rows)
        self.turn_index = 0
        calculate_legal_moves(position, turn_index)

    def __init__(self, pieces, turn_index):
        self.pieces = pieces
        self.turn_index = turn_index
        calculate_legal_moves(position, turn_index)
