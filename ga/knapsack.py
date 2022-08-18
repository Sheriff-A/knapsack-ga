from utils.config import Config
from typing import List

import numpy as np
import random


def calculate_fitness(chromosome: List[int], bank: List[int], budget: int):
    score = 0
    for idx, gene in enumerate(chromosome):
        if gene == 1:
            score += bank[idx]
        if score > budget:
            return 0
    return score


class Knapsack:
    def __init__(self, config: Config, chromosome: List[int] = None):
        gene_length = config.get('bank_length')
        if chromosome is None:
            chromosome = np.random.randint(0, 2, gene_length)

        self.chromosome = chromosome
        self.fitness = 0

    # Mutation Algorithm: Bit Flip Mutation
    def mutate(self):
        chromosome_length = len(self.chromosome)
        size = np.random.randint(0, chromosome_length)
        idx = random.sample(range(chromosome_length), size)
        for i in idx:
            self.chromosome[i] = 1 if self.chromosome[i] == 0 else 0

    def get_fitness(self, bank, budget):
        self.fitness = calculate_fitness(self.chromosome, bank, budget)

    def __repr__(self):
        return f'Selection: {self.chromosome} - Fitness: {self.fitness}'

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness
