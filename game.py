import numpy as np
from enum import Enum


class Action(Enum):
    STAY = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class Game:
    def __init__(self, size=12, num_agents=1, ratio=0.2):
        # init random
        self.seed = 42
        np.random.seed(self.seed)

        # init grid
        self.size = (size, size)
        self.ratio = ratio
        self.grid = (np.random.random((self.size)) < ratio).astype(int)
        self.score = [0 for i in range(num_agents)]

        # create agents
        self.num_agents = num_agents
        assert num_agents <= 4, "Maximum of 4 agents allowed."
        self.pos = [(0, 0), (self.size), (0, self.size[1]), (self.size[0], 0)][
            :num_agents
        ]

    def get_info(self):
        info = {}
        info["num_agents"] = self.num_agents
        return info

    def step(self, action, agent):
        if action is None:
            raise AssertionError("Action cannot be None")
        if agent is None:
            raise AssertionError("Agent cannot be None")
        if agent < 0 or agent >= self.num_agents:
            raise AssertionError("Agent must be between 0 and num_agents")

    def reset(self):
        self.grid = (np.random.random((self.size)) < self.ratio).astype(int)
        self.pos = [(0, 0), (self.size), (0, self.size[1]), (self.size[0], 0)][
            :self.num_agents
        ]
        self.score = [0 for i in range(self.num_agents)]

    def render(self):
        np.set_printoptions(formatter={"all": lambda x: str(x)})
        render_grid = self.grid.astype(str)
        render_grid = np.char.replace(render_grid, "1", "x")
        render_grid = np.char.replace(render_grid, "0", " ")
        print(render_grid)
        print(self.pos)
