from utils.parser import command_parser
from utils.config import Config
from utils.random import RandomNumberGenerator


def random_knapsack(config: Config):
    print('Random Knapsack')
    seed = config.get('seed')
    print(f'Seed: {seed}')
    rng = RandomNumberGenerator(seed)
    print(rng.get_random())


if __name__ == '__main__':
    parser = command_parser()
    parse_args = parser.parse_args()
    print(parse_args)
    args = vars(parse_args)
    command = args.pop('command')
    print(command)

    if command == 'random':
        config = Config(**args)
        print(f'Config: {config}')
        random_knapsack(config)

    else:
        print(f'Command ({command}) Not Found')
