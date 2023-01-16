class Move:

    # Constructor
    def __init__(self, piece, destination_square):
        self.__piece = piece
        self.__destination_square = destination_square

    # Getters & Setters
    def get_piece(self):
        return self.__piece

    def set_piece(self, piece):
        self.__piece = piece

    def get_destination_square(self):
        return self.__destination_square

    def set_destination_square(self, destination_square):
        self.__destination_square = destination_square
