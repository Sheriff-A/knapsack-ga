from ga.knapsack import Knapsack

class GeneticAlgorithm:
    def __init__(self, config):
        max_pop = config.get('max_population')
        self.population = [Knapsack(config)] * max_pop
        print(self.population)
