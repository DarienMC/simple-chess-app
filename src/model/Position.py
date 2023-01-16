import numpy as np
import math

from Piece import *


def generate_standard_position():
    # empty board
    standard_position = np.empty([8, 8], dtype=None)

    # white pieces
    standard_position[0][0] = Rook(0)
    standard_position[0][1] = Knight(0)
    standard_position[0][2] = Bishop(0)
    standard_position[0][3] = Queen(0)
    standard_position[0][4] = King(0)
    standard_position[0][5] = Bishop(0)
    standard_position[0][6] = Knight(0)
    standard_position[0][7] = Rook(0)

    standard_position[1][0] = Pawn(0)
    standard_position[1][1] = Pawn(0)
    standard_position[1][2] = Pawn(0)
    standard_position[1][3] = Pawn(0)
    standard_position[1][4] = Pawn(0)
    standard_position[1][5] = Pawn(0)
    standard_position[1][6] = Pawn(0)
    standard_position[1][7] = Pawn(0)

    # black pieces
    standard_position[7][0] = Rook(1)
    standard_position[7][1] = Knight(1)
    standard_position[7][2] = Bishop(1)
    standard_position[7][3] = Queen(1)
    standard_position[7][4] = King(1)
    standard_position[7][5] = Bishop(1)
    standard_position[7][6] = Knight(1)
    standard_position[7][7] = Rook(1)

    standard_position[6][0] = Pawn(1)
    standard_position[6][1] = Pawn(1)
    standard_position[6][2] = Pawn(1)
    standard_position[6][3] = Pawn(1)
    standard_position[6][4] = Pawn(1)
    standard_position[6][5] = Pawn(1)
    standard_position[6][6] = Pawn(1)
    standard_position[6][7] = Pawn(1)

    return standard_position


def calculate_legal_moves():
    return []


class Position:
    # Class attributes
    __columns = 8
    __rows = 8
    __in_check = False
    __legal_moves = None

    # Constructor
    def __init__(self):
        self.__board = generate_standard_position()
        self.__turn_index = 0
        self.__legal_moves = calculate_legal_moves()

    def __init__(self, board, turn_index):
        self.__board = board
        self.__turn_index = turn_index
        self.__legal_moves = calculate_legal_moves()

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

