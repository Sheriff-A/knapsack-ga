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
    # Minimum Price
    subps_random.add_argument(
        '--min_price',
        type=int,
        default=100,
        help="Minimum Value For List of Knapsack Items"
    )

    # Maximum Price
    subps_random.add_argument(
        '--max_price',
        type=int,
        default=1000,
        help="Maximum Value For List of Knapsack Items"
    )

    # Bank Length
    subps_random.add_argument(
        "--bank_length",
        type=int,
        default=20,
        help="Number of Items in the Bank of Items for the Knapsack"
    )

    # Budget
    subps_random.add_argument(
        '--budget',
        type=int,
        default=5000,
        help="Target Value for Knapsack"
    )

    # Training Parameters
    # Population Size
    subps_random.add_argument(
        '--population_size',
        type=int,
        default=8,
        help="Number of Knapsacks in the Population"
    )

    # Number of Generations
    subps_random.add_argument(
        '--num_generation',
        type=int,
        default=8,
        help="Maximum Number of Generations to Train on"
    )

    # Show Population
    subps_random.add_argument(
        '--show_population',
        action='store_true',
        help="Toggle to Show Population after Every Generation"
    )

    subps_random.add_argument(
        '--population_cutoff_threshold',
        type=float,
        default=.6,
        help="Threshold to Select Top Members from to be used in Crossover"
    )

    subps_random.add_argument(
        '--crossover_rate',
        type=float,
        default=.8,
        help="Probability of Applying Crossover"
    )

    subps_random.add_argument(
        '--mutation_rate',
        type=float,
        default=.1,
        help="Probability of Applying Mutation"
    )

    subps_random.add_argument(
        '--num_elites',
        type=int,
        default=2,
        help="Number of Members to Select with Elitism"
    )

    subps_random.set_defaults(command='random')

    return parser
