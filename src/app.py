"""
The app.py module is the pseudo-entry point of our project.
"""
from model.Game import Game
from model.Player import Player


def run():
    player1 = Player('White')
    player2 = Player('Black')

    game = Game([player1, player2])
    game.play()
