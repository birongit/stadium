import sys
import pytest
from game import Game
from game import Action


def test_game():
    game = Game(num_agents=3)

    assert game is not None

    num_agents = game.get_info()["num_agents"]

    # These calls are not allowed
    with pytest.raises(AssertionError):
        game.step(None, None)
        game.step(None, 0)
        game.step(Action.STAY, -1)
        game.step(Action.Stay, num_agents)

    # These calls are allowed
    [game.step(Action.STAY, agent) for agent in range(num_agents)]

    game.render()
    game.reset()


print(sys.version)
test_game()
