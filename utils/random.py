import numpy as np


class RandomNumberGenerator:
    def __init__(self, seed):
        self.rng = np.random.default_rng(seed)

    def get_random(self, shape: int or tuple = None):
        if shape is None:
            return self.rng.random()
        return self.rng.random(shape)
