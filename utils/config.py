import random

DEFAULTS = {
    #     Random
    'seed': 123
}


def get_random_seed(seed: int = None):
    if seed is None:
        seed = random.randint(0, 2 ** 32 - 1)
    return seed


class Config:
    def __init__(self, **opts):
        params = DEFAULTS.copy()
        for opt in opts:
            if opt not in params:
                continue
            params[opt] = opts[opt]

        params['seed'] = get_random_seed(opts['seed'])

        self._PARAMS = params

    def get(self, attr):
        if attr in self._PARAMS:
            return self._PARAMS[attr]
        raise ValueError(f'{self} does not contain attribute {attr}.')

    def set(self, attr, value):
        if attr in self._PARAMS:
            self._PARAMS[attr] = value
        else:
            raise ValueError(f'{self} does not contain attribute {attr}.')

    def __repr__(self):
        return str(self._PARAMS)
