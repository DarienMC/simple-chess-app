from abc import ABC, abstractmethod
import Position, Move

class Piece(ABC):
    # Class attributes
    __has_moved = False

    @abstractmethod
    def __get_movement(self):
        pass

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
    def __get_movement(self):
        return {
            (0,1),
            (1,1),
            (1,0),
            (1,-1),
            (0,-1),
            (-1,-1),
            (-1,0),
            (-1,1)
        }

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
    def __get_movement(self):
        return {
            (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
            (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7),
            (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
            (1,-1),(2,-2), (3,-3), (4,-4), (5,-5), (6,-6), (7,-7),
            (0,-1),(0,-2), (0,-3), (0,-4), (0,-5), (0,-6), (0,-7),
            (-1,-1),(-2,-2), (-3,-3), (-4,-4), (-5,-5), (-6,-6), (-7,-7),
            (-1,0),(-2,0), (-3,0), (-4,0), (-5,0), (-6,0), (-7,0),
            (-1,1), (-2,2), (-3,3), (-4,4), (-5,5), (-6,6), (-7,7)
        }

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
    def __get_movement(self):
        return {
            (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
            (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
            (0,-1),(0,-2), (0,-3), (0,-4), (0,-5), (0,-6), (0,-7),
            (-1,0),(-2,0), (-3,0), (-4,0), (-5,0), (-6,0), (-7,0),
        }

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
    def __get_movement(self):
        return {
            (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7),
            (1,-1),(2,-2), (3,-3), (4,-4), (5,-5), (6,-6), (7,-7),
            (-1,-1),(-2,-2), (-3,-3), (-4,-4), (-5,-5), (-6,-6), (-7,-7),
            (-1,1), (-2,2), (-3,3), (-4,4), (-5,5), (-6,6), (-7,7)
        }

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
    def __get_movement(self):
        return {
            (2,1),
            (1,2),
            (-1,2),
            (-2,1),
            (-2,-1),
            (-1,-2),
            (1,-2),
            (2, -1),
        }

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
    def __get_movement(self):
        if (self.__color is 0):
            if (self.__has_moved is False):
                return {
                    (0,1), (0,2)
                }
            else:
                return {
                    (0,1)
                }
        elif (self.__color is 1):
            if (self.__has_moved is False):
                return {
                    (0,-1), (0,-2)
                }
            else:
                return {
                    (0,-1)
                }

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
