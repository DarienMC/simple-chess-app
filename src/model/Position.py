import numpy as np
import Piece, Move


def initialize_standard_position():
    # empty board
    standard_position = np.empty([columns, rows],dtype=Piece)

    # white pieces
    standard_position[0][0] = Rook  (0, (0,0))
    standard_position[0][1] = Knight(0, (0,1))
    standard_position[0][2] = Bishop(0, (0,2))
    standard_position[0][3] = Queen (0, (0,3))
    standard_position[0][4] = King  (0, (0,4))
    standard_position[0][5] = Bishop(0, (0,5))
    standard_position[0][6] = Knight(0, (0,6))
    standard_position[0][7] = Rook  (0, (0,7))

    standard_position[1][0] = Pawn(0, (1,0))
    standard_position[1][1] = Pawn(0, (1,1))
    standard_position[1][2] = Pawn(0, (1,2))
    standard_position[1][3] = Pawn(0, (1,3))
    standard_position[1][4] = Pawn(0, (1,4))
    standard_position[1][5] = Pawn(0, (1,5))
    standard_position[1][6] = Pawn(0, (1,6))
    standard_position[1][7] = Pawn(0, (1,7))

    # black pieces
    standard_position[7][0] = Rook  (1, (7,0))
    standard_position[7][1] = Knight(1, (7,1))
    standard_position[7][2] = Bishop(1, (7,2))
    standard_position[7][3] = Queen (1, (7,3))
    standard_position[7][4] = King  (1, (7,4))
    standard_position[7][5] = Bishop(1, (7,5))
    standard_position[7][6] = Knight(1, (7,6))
    standard_position[7][7] = Rook  (1, (7,7))

    standard_position[6][0] = Pawn(1, (7,0))
    standard_position[6][1] = Pawn(1, (7,1))
    standard_position[6][2] = Pawn(1, (7,2))
    standard_position[6][3] = Pawn(1, (7,3))
    standard_position[6][4] = Pawn(1, (7,4))
    standard_position[6][5] = Pawn(1, (7,5))
    standard_position[6][6] = Pawn(1, (7,6))
    standard_position[6][7] = Pawn(1, (7,7))

    return standard_position


class Position:
    # Class attributes
    columns = 8
    rows = 8
    in_check = False
    legal_moves = None

    def calculate_legal_moves(self, pieces, turn_index):
        pass


    # Constructor
    def __init__(self):
        self.position = initialize_standard_position()
        self.turn_index = 0
        self.legal_moves = calculate_legal_moves(self.position, self.turn_index)

    def __init__(self, position, turn_index):
        self.position = position
        self.turn_index = turn_index
        self.legal_moves = calculate_legal_moves(position, turn_index)
