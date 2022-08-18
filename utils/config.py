import random
import numpy as np

DEFAULTS = {
    # General
    'seed': 123,

    # Dataset
    'min_price': 100,
    'max_price': 1000,
    'bank_length': 20,
    'budget': 5000,

    # Training
    'population_size': 8,
    'num_generation': 10,
    'show_population': False,
}


def set_random_seed(seed: int = None):
    if seed is None:
        seed = random.randint(0, 2 ** 32 - 1)
    np.random.seed(seed)
    return seed


class Config:
    def __init__(self, **opts):
        params = DEFAULTS.copy()
        for opt in opts:
            if opt not in params:
                continue
            params[opt] = opts[opt]

        params['seed'] = set_random_seed(opts['seed'])

        self._PARAMS = params

    def get(self, attr: str):
        if attr in self._PARAMS:
            return self._PARAMS[attr]
        raise ValueError(f'{self} does not contain attribute {attr}.')

    def set(self, attr: str, value):
        if attr in self._PARAMS:
            self._PARAMS[attr] = value
        else:
            raise ValueError(f'{self} does not contain attribute {attr}.')

    def __repr__(self):
        return str(self._PARAMS)
