from utils.parser import command_parser
from utils.config import Config

from data.dataset import RandomDataset
from ga.ga import GeneticAlgorithm


def random_knapsack(config: Config):
    print('Random Knapsack')
    data = RandomDataset(config)
    ga = GeneticAlgorithm(config, data)
    ga.train()


if __name__ == '__main__':
    parser = command_parser()
    parse_args = parser.parse_args()
    print(parse_args)
    args = vars(parse_args)
    command = args.pop('command')
    print(command)

    if command == 'random':
        configuration = Config(**args)
        print(f'Config: {configuration}')
        random_knapsack(configuration)

    else:
        print(f'Command ({command}) Not Found')
