import click
import pandas as pd
import numpy as np
import influans_putup.simple_recurcive_strategy as srs

@click.command()
@click.option('--data', help='csv', required=True)
def simple_recursive_strategy(data):
    data = pd.read_csv(data, header=None)
    maximum_reward = srs.simple_recursive_strategy(np.array(data[0]))
    print(maximum_reward)
