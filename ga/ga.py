from ga.knapsack import Knapsack
from data.dataset import RandomDataset

from typing import List

class GeneticAlgorithm:
    def __init__(self, config, data: RandomDataset):
        max_pop = config.get('population_size')
        population = []
        for _ in range(max_pop):
            population.append(Knapsack(config, data.bank, data.budget))
        self.population = population
        self.num_generations = config.get('num_generation')
        self.show_population = config.get('show_population')
        self.target = data.budget

    def train(self):
        def sort_list(population: List[Knapsack]):
            return sorted(population)

        for g in range(self.num_generations):
            print(f'\n--- Generation {g} ---')

            # Sort By Fitness
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
            print(f'Accuracy: {accuracy * 100:.2f}%')
            if accuracy == 1:
                break
