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
    with pytest.raises(AssertionError):
        game.step(None, 0)
    with pytest.raises(AssertionError):
        game.step(Action.STAY, None)
    with pytest.raises(AssertionError):
        game.step(Action.STAY, -1)
    with pytest.raises(AssertionError):
        game.step(Action.STAY, num_agents)

    # These calls are allowed
    [game.step(Action.STAY, agent) for agent in range(num_agents)]

    game.render()
    game.reset()


print(sys.version)
test_game()
