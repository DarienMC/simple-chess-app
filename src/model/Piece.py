from abc import ABC, abstractmethod
import Position, Move

class Piece(ABC):
    # Class attributes
    has_moved = False

    @abstractmethod
    def calculate_legal_moves(self, position):
        pass

    # Constructor
    def __init__(self, color, occupied_square):
        self.color = color
        self.occupied_square = occupied_square

class King(Piece):
    def calculate_legal_moves(self, position):
        pass

class Queen(Piece):
    def calculate_legal_moves(self, position):
        pass

class Rook(Piece):
    def calculate_legal_moves(self, position):
        pass

class Bishop(Piece):
    def calculate_legal_moves(self, position):
        pass

class Knight(Piece):
    def calculate_legal_moves(self, position):
        pass

class Pawn(Piece):
    def calculate_legal_moves(self, position):
        pass

class ShadowPawn(Piece):
    def calculate_legal_moves(self, position):
        return None