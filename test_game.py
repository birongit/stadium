import sys
from game import Game

print(sys.version)

game = Game(num_agents=3)

assert game is not None

game.step(None)
game.render()
game.reset()
