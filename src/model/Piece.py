import numpy as np
from abc import ABC, abstractmethod


class Piece(ABC):
    # Constructor
    def __init__(self, color, has_moved=False):
        self.__color = color
        self.__has_moved = has_moved

    # Methods
    @abstractmethod
    def get_movement(self):
        raise NotImplementedError

    @abstractmethod
    def get_capture_movement(self):
        raise NotImplementedError

    @abstractmethod
    def get_unicode(self):
        raise NotImplementedError

    @abstractmethod
    def get_abbreviation(self):
        raise NotImplementedError

    # Getters & Setters
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_has_moved(self):
        return self.__has_moved

    def set_has_moved(self, has_moved):
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
        if self.get_color() == 0:
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
        if self.get_color() == 0:
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
        if self.get_color() == 0:
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
        if self.get_color() == 0:
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
        if self.get_color() == 0:
            return '♘'
        else:
            return '♞'

    def get_abbreviation(self):
        return 'N'


class Pawn(Piece):
    # Implement Abstract Methods
    def get_movement(self):
        if self.get_color() == 0:
            if self.get_has_moved() is False:
                return {
                    (0, 1), (0, 2)
                }
            else:
                return {
                    (0, 1)
                }
        elif self.get_color() == 1:
            if self.get_has_moved() is False:
                return {
                    (0, -1), (0, -2)
                }
            else:
                return {
                    (0, -1)
                }

    def get_capture_movement(self):
        if self.get_color() == 0:
            return {
                    (-1, 1), (1, 1)
            }
        elif self.get_color() == 1:
            return {
                    (-1, -1), (1, -1)
            }

    def get_unicode(self):
        if self.get_color() == 0:
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
        return ' '

    def get_abbreviation(self):
        return ' '
