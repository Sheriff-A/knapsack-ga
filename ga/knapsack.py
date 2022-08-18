from utils.config import Config
from typing import List

import numpy as np


def calculate_fitness(chromosome: List[int], bank: List[int], budget: int):
    score = 0
    for idx, gene in enumerate(chromosome):
        if gene == 1:
            score += bank[idx]
        if score > budget:
            return 0
    return score


class Knapsack:
    def __init__(self, config: Config, bank: List[int], budget: int, chromosome: List[int] = None):
        gene_length = config.get('bank_length')
        if chromosome is None:
            chromosome = np.random.randint(0, 2, gene_length)

        self.chromosome = chromosome
        self.fitness = calculate_fitness(self.chromosome, bank, budget)

    def mutate(self):
        print('Apply Mutation')

    def __repr__(self):
        return f'Solution: {self.chromosome} - Fitness: {self.fitness}'

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness
