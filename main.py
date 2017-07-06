import click
import pandas as pd
import numpy as np
import influans_putup.simple_recurcive_strategy as srs
import influans_putup.heuristic_recursive_strategy as hrs
import influans_putup.second_recurcive_strategy as srs_2
import time

@click.command()
@click.option('--data', help='csv', required=True)
def simple_recursive_strategy(data):
    # Read data with pandas is faster (laziest solution)
    data = pd.read_csv(data, header=None)
    now = time.time()
    maximum_reward = srs.simple_recursive_strategy(np.array(data[0]))
    print(maximum_reward)
    print("Execution time = " + str(time.time() - now))

@click.command()
@click.option('--data', help='csv', required=True)
def heuristic_recursive_strategy(data):
    # Read data with pandas is faster (laziest solution)
    data = pd.read_csv(data, header=None)
    now = time.time()
    maximum_reward = hrs.heuristic_recursive_strategy(np.array(data[0]))
    print(maximum_reward)
    print("Execution time = " + str(time.time() - now))

@click.command()
@click.option('--data', help='csv', required=True)
def second_recursive_strategy(data):
    # Read data with pandas is faster (laziest solution)
    data = pd.read_csv(data, header=None)
    now = time.time()
    maximum_reward = srs_2.second_recursive_strategy(np.array(data[0]))
    print(maximum_reward)
    print("Execution time = " + str(time.time() - now))
