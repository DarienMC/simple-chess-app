"""
The app.py module is the pseudo-entry point of our project.
"""
import model

def run():
    player1 = Player('White')
    player2 = Player('Black')

    game = Game([player1, player2])
    game.play()