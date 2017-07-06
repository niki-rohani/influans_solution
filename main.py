import click
import pandas as pd
import numpy as np
import influans_putup.simple_recurcive_strategy as srs
import influans_putup.heuristic_recursive_strategy as hrs

@click.command()
@click.option('--data', help='csv', required=True)
def simple_recursive_strategy(data):
    # Read data with pandas is faster (laziest solution)
    data = pd.read_csv(data, header=None)
    maximum_reward = srs.simple_recursive_strategy(np.array(data[0]))
    print(maximum_reward)

@click.command()
@click.option('--data', help='csv', required=True)
def heuristic_recursive_strategy(data):
    # Read data with pandas is faster (laziest solution)
    data = pd.read_csv(data, header=None)
    maximum_reward = hrs.heuristic_recursive_strategy(np.array(data[0]))
    print(maximum_reward)
