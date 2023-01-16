from enum import Enum

from Position import Position


class GameState(Enum):
    IN_PROGRESS = 1
    WHITE_WINS = 2
    BLACK_WINS = 3
    DRAW = 4


def print_current_position_as_text():
    print(
        '    a   b   c   d   e   f   g   h    '
        '  =================================  '
        '8 | R | N | B | Q | K | B | N | R | 8'
        '7 | P | P | P | P | P | P | P | P | 7'
        '6 |   |   |   |   |   |   |   |   | 6'
        '5 |   |   |   |   |   |   |   |   | 5'
        '4 |   |   |   |   |   |   |   |   | 4'
        '3 |   |   |   |   |   |   |   |   | 3'
        '2 | P | P | P | P | P | P | P | P | 2'
        '1 | R | N | B | Q | K | B | N | R | 1'
        '  =================================  '
        '    a   b   c   d   e   f   g   h    '
    )


def change_to_subsequent_position():
    return Position


class Game:
    __state = GameState.IN_PROGRESS
    __current_position = Position
    __moves = None

    # Constructor
    def __init__(self, players):
        self.__players = players

    def play(self):
        while self.__state is GameState.IN_PROGRESS:
            if self.__current_position.get_legal_moves is not None:
                move = input(f'{self.__players[self.__current_position.get_turn_index]} to move: ')
                change_to_subsequent_position()
            else:
                if self.__current_position.get_in_check:
                    if self.__current_position.get_turn_index is 0:
                        self.__state = GameState.WHITE_WINS
                    else:
                        self.__state = GameState.BLACK_WINS
                else:
                    self.__state = GameState.DRAW

    # Getters & Setters
    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_current_position(self):
        return self.__current_position

    def set_current_position(self, current_position):
        self.__current_position = current_position

    def get_moves(self):
        return self.__moves

    def set_moves(self, moves):
        self.__moves = moves

    def get_players(self):
        return self.__players

    def set_players(self, players):
        self.__players = players
