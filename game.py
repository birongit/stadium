import numpy as np


class Game:
    def __init__(self, size=12, num_agents=1, ratio=0.2):
        # init random
        self.seed = 42
        np.random.seed(self.seed)

        # init grid
        self.size = (size, size)
        self.ratio = ratio
        self.grid = (np.random.random((self.size)) < ratio).astype(int)

        # create agents
        self.num_agents = num_agents
        assert num_agents <= 4, "Maximum of 4 agents allowed."
        self.pos = [(0, 0), (self.size), (0, self.size[1]), (self.size[0], 0)][
            :num_agents
        ]

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        np.set_printoptions(formatter={"all": lambda x: str(x)})
        render_grid = self.grid.astype(str)
        render_grid = np.char.replace(render_grid, "1", "x")
        render_grid = np.char.replace(render_grid, "0", " ")
        print(render_grid)
        print(self.pos)
