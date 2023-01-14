from abc import ABC, abstractmethod
import Position, Move

class Piece(ABC):
    # Class attributes
    __has_moved = False

    @abstractmethod
    def calculate_legal_moves(self, position):
        pass

    @abstractmethod
    def get_unicode(self):
        pass

    @abstractmethod
    def get_abbreviation(self):
        pass

    # Constructor
    def __init__(self, color, occupied_square):
        self.__color = color
        self.__occupied_square = occupied_square


class King(Piece):
    def calculate_legal_moves(self, position):
        pass

    def get_unicode(self):
        if self.__color is 0:
            return '♔'
        else:
            return '♚'

    def get_abbreviation(self):
        return 'K'


class Queen(Piece):
    def calculate_legal_moves(self, position):
        pass

    def get_unicode(self):
        if self.__color is 0:
            return '♕'
        else:
            return '♛'

    def get_abbreviation(self):
        return 'Q'


class Rook(Piece):
    def calculate_legal_moves(self, position):
        pass

    def get_unicode(self):
        if self.__color is 0:
            return '♖'
        else:
            return '♜'

    def get_abbreviation(self):
        return 'R'


class Bishop(Piece):
    def calculate_legal_moves(self, position):
        pass

    def get_unicode(self):
        if self.__color is 0:
            return '♗'
        else:
            return '♝'

    def get_abbreviation(self):
        return 'B'


class Knight(Piece):
    def calculate_legal_moves(self, position):
        pass

    def get_unicode(self):
        if self.__color is 0:
            return '♘'
        else:
            return '♞'

    def get_abbreviation(self):
        return 'N'


class Pawn(Piece):
    def calculate_legal_moves(self, position):
        pass

    def get_unicode(self):
        if self.__color is 0:
            return '♙'
        else:
            return '♟︎'

    def get_abbreviation(self):
        return 'P'


class ShadowPawn(Piece):
    def calculate_legal_moves(self, position):
        return None

    def get_unicode(self):
        return None

    def get_abbreviation(self):
        return None
