from ga.knapsack import Knapsack
from data.dataset import RandomDataset
import numpy as np
import copy

from typing import List


class GeneticAlgorithm:
    def __init__(self, config, data: RandomDataset):
        max_pop = config.get('population_size')
        population = []
        for _ in range(max_pop):
            population.append(Knapsack(config))
        self.population = population
        self.num_generations = config.get('num_generation')
        self.show_population = config.get('show_population')
        self.mutation_rate = config.get("mutation_rate")
        self.crossover_rate = config.get("crossover_rate")
        self.threshold = config.get("population_cutoff_threshold")
        self.bank = data.bank
        self.target = data.budget

    def train(self):

        best_member = None

        def create_offspring(n: int, crossover_rate: float, mutation_rate: float, pool: List[Knapsack]):
            offspring = []

            for _ in range(int(n / 2)):
                idx1 = np.random.randint(0, len(pool))
                idx2 = np.random.randint(0, len(pool))
                while idx2 != idx1:
                    idx2 = np.random.randint(0, len(pool))

                # print(f"Index 1: {idx1} - Index 2: {idx2}")
                parent1 = pool[idx1]
                parent2 = pool[idx2]
                offspring1 = copy.deepcopy(parent1)
                offspring2 = copy.deepcopy(parent2)

                # Crossover: Single Point Crossover
                crossover_chance = np.random.random()
                if crossover_chance <= crossover_rate:
                    crossover_point = np.random.randint(0, len(parent1.chromosome))
                    mask = [0] * len(parent1.chromosome)
                    mask[:crossover_point] = [1] * crossover_point
                    # print(f"Mask: {mask}")

                    offspring1.chromosome[crossover_point:] = copy.deepcopy(parent2.chromosome[crossover_point:])
                    offspring2.chromosome[crossover_point:] = copy.deepcopy(parent1.chromosome[crossover_point:])

                # Mutation
                mutation_chance = np.random.random()
                if mutation_chance <= mutation_rate:
                    offspring1.mutate()
                    offspring2.mutate()

                offspring.append(offspring1)
                offspring.append(offspring2)

            return offspring

        for g in range(self.num_generations):
            print(f'\n--- Generation {g} ---')

            # Calculate Fitness
            for sack in self.population:
                sack.get_fitness(self.bank, self.target)

            # Sort By Fitness
            # Higher Fitness is Better
            self.population.sort(reverse=True)

            if self.show_population:
                print('--- Current Population ---')
                for sack in self.population:
                    print(sack)

            # Select Best Member
            best_member = self.population[0]
            print(f'Best Member: {best_member}')

            # Check if we have reached out goal
            accuracy = best_member.fitness / self.target
            print(f'Utilization: {accuracy * 100:.2f}%')
            if accuracy == 1:
                break

            # Selection Algorithm: Elitism
            first_best = self.population[0]
            second_best = self.population[1]

            cutoff_mark = int(self.threshold * len(self.population))

            new_population = [first_best, second_best]
            reproduction_pool = self.population[:cutoff_mark]

            new_offspring = create_offspring(len(self.population) - 2, self.crossover_rate, self.mutation_rate,
                                             reproduction_pool)

            new_population.extend(new_offspring)

            self.population = new_population

        return best_member
