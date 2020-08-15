import sys
from game import Game


def test_game():
    game = Game(num_agents=3)

    assert game is not None

    game.step(None)
    game.render()
    game.reset()


print(sys.version)
test_game()
