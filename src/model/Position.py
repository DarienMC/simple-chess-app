import numpy as np
import math

from model.Piece import *


def generate_standard_position():
    # empty board
    standard_position = np.empty([8, 8], dtype=Piece)

    # white pieces
    standard_position[0][0] = Rook(0)
    standard_position[1][0] = Knight(0)
    standard_position[2][0] = Bishop(0)
    standard_position[3][0] = Queen(0)
    standard_position[4][0] = King(0)
    standard_position[5][0] = Bishop(0)
    standard_position[6][0] = Knight(0)
    standard_position[7][0] = Rook(0)

    standard_position[0][1] = Pawn(0)
    standard_position[1][1] = Pawn(0)
    standard_position[2][1] = Pawn(0)
    standard_position[3][1] = Pawn(0)
    standard_position[4][1] = Pawn(0)
    standard_position[5][1] = Pawn(0)
    standard_position[6][1] = Pawn(0)
    standard_position[7][1] = Pawn(0)

    # black pieces
    standard_position[0][7] = Rook(1)
    standard_position[1][7] = Knight(1)
    standard_position[2][7] = Bishop(1)
    standard_position[3][7] = Queen(1)
    standard_position[4][7] = King(1)
    standard_position[5][7] = Bishop(1)
    standard_position[6][7] = Knight(1)
    standard_position[7][7] = Rook(1)

    standard_position[0][6] = Pawn(1)
    standard_position[1][6] = Pawn(1)
    standard_position[2][6] = Pawn(1)
    standard_position[3][6] = Pawn(1)
    standard_position[4][6] = Pawn(1)
    standard_position[5][6] = Pawn(1)
    standard_position[6][6] = Pawn(1)
    standard_position[7][6] = Pawn(1)

    return standard_position


def calculate_legal_moves():
    return []


def determine_in_check():
    return False


class Position:
    # Constructor
    def __init__(self, turn_index=0):
        self.__turn_index = turn_index
        self.__board = generate_standard_position()
        self.__in_check = determine_in_check()
        self.__legal_moves = calculate_legal_moves()

    # Methods
    def print_board(self):
        num_files = len(self.__board)
        num_ranks = len(self.__board[0])
        text = \
            '    a   b   c   d   e   f   g   h    \n' \
            '  =================================  '
        for i in range(num_ranks):
            text = f'{text}\n' \
                   f'{num_files-i} |'
            for j in range(num_files):
                if isinstance(self.__board[j][i], Piece):
                    text = f'{text} {self.__board[j][i].get_unicode()} |'
                else:
                    text = f'{text}   |'

        text = f'{text}\n' \
               f'  =================================  \n'

        print(f'{text}')

    # Getters & Setters
    def get_board(self):
        return self.__board

    def set_board(self, board):
        self.__board = board

    def get_in_check(self):
        return self.__in_check

    def set_in_check(self, in_check):
        self.__in_check = in_check

    def get_turn_index(self):
        return self.__turn_index

    def set_turn_index(self, turn_index):
        self.__turn_index = turn_index

    def get_legal_moves(self):
        return self.__legal_moves

    def set_legal_moves(self, legal_moves):
        self.__legal_moves = legal_moves
