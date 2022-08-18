import argparse


def command_parser():
    parser = argparse.ArgumentParser()
    subps = parser.add_subparsers()

    '''
        Solves Knapsack Problem Using Randomly Initialized Dataset
    '''
    subps_random = subps.add_parser(
        'random',
        help='Solve Random Knapsack Problem'
    )

    # Seed
    subps_random.add_argument(
        '--seed',
        type=int,
        help='Random Initializer Seed'
    )

    subps_random.set_defaults(command='random')

    return parser
