from utils.config import Config

import numpy as np


class RandomDataset:
    def __init__(self, config: Config):

        print(f'Seed: {config.get("seed")}')

        bank_length = config.get('bank_length')
        min_price = config.get('min_price')
        max_price = config.get('max_price')

        self.budget = config.get('budget')
        self.bank = np.random.randint(min_price, max_price, bank_length)

        print(f'Bank: {self.bank}')

