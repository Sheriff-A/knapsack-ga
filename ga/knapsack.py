from utils.config import Config
from data.dataset import RandomDataset

import numpy as np


def calculate_fitness(solution: [int]):
    print(solution)
    return 0


class Knapsack:
    def __init__(self, config: Config):
        gene_length = config.get('gene_length')

        self.solution = np.random.randint(0, 2, gene_length)
        self.fitness = calculate_fitness(self.solution)

    def mutate(self):
        print('Apply Mutation')

    def __repr__(self):
        return f'Solution: {self.solution} - Fitness: {self.fitness}'
