"""
The app.py module is the pseudo-entry point of our project.
"""
from model.Game import Game
from model.Player import Player
from model.Position import Position


def run():
    player1 = Player('White')
    player2 = Player('Black')

    game = Game([player1, player2])
    var = game.get_current_position().print_board()

