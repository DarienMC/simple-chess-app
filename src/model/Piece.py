import numpy as np
from abc import ABC, abstractmethod


class Piece(ABC):
    # Class attributes
    __has_moved = False

    # Constructor
    def __init__(self, color):
        self.__color = color

    # Methods
    @abstractmethod
    def get_movement(self):
        pass

    @abstractmethod
    def get_capture_movement(self):
        pass

    @abstractmethod
    def get_unicode(self):
        pass

    @abstractmethod
    def get_abbreviation(self):
        pass

    # Getters & Setters
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_has_moved(self):
        return self.__has_moved

    def set_turn_index(self, has_moved):
        self.__has_moved = has_moved


class King(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        return {
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1)
        }

    def get_capture_movement(self):
        return self.get_movement()

    def get_unicode(self):
        if self.__color == 0:
            return '♔'
        else:
            return '♚'

    def get_abbreviation(self):
        return 'K'


class Queen(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        return {
            (0, np.inf),
            (np.inf, np.inf),
            (np.inf, 0),
            (np.inf, -np.inf),
            (0, -np.inf),
            (-np.inf, -np.inf),
            (-np.inf, 0),
            (-np.inf, np.inf)
        }

    def get_capture_movement(self):
        return self.get_movement()

    def get_unicode(self):
        if self.__color == 0:
            return '♕'
        else:
            return '♛'

    def get_abbreviation(self):
        return 'Q'


class Rook(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        return {
            (0, np.inf),
            (np.inf, 0),
            (0, -np.inf),
            (-np.inf, 0)
        }

    def get_capture_movement(self):
        return self.get_movement()

    def get_unicode(self):
        if self.__color == 0:
            return '♖'
        else:
            return '♜'

    def get_abbreviation(self):
        return 'R'


class Bishop(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        return {
            (np.inf, np.inf),
            (np.inf, -np.inf),
            (-np.inf, -np.inf),
            (-np.inf, np.inf)
        }

    def get_capture_movement(self):
        return self.get_movement()

    def get_unicode(self):
        if self.__color == 0:
            return '♗'
        else:
            return '♝'

    def get_abbreviation(self):
        return 'B'


class Knight(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        return {
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1)
        }

    def get_capture_movement(self):
        return self.get_movement()

    def get_unicode(self):
        if self.__color == 0:
            return '♘'
        else:
            return '♞'

    def get_abbreviation(self):
        return 'N'


class Pawn(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        if self.__color == 0:
            if self.__has_moved is False:
                return {
                    (0, 1), (0, 2)
                }
            else:
                return {
                    (0, 1)
                }
        elif self.__color == 1:
            if self.__has_moved is False:
                return {
                    (0, -1), (0, -2)
                }
            else:
                return {
                    (0, -1)
                }

    def get_capture_movement(self):
        if self.__color == 0:
            return {
                    (-1, 1), (1, 1)
            }
        elif self.__color == 1:
            return {
                    (-1, -1), (1, -1)
            }

    def get_unicode(self):
        if self.__color == 0:
            return '♙'
        else:
            return '♟︎'

    def get_abbreviation(self):
        return 'P'


class ShadowPawn(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        return None

    def get_capture_movement(self):
        return None

    def get_unicode(self):
        return None

    def get_abbreviation(self):
        return ' '
