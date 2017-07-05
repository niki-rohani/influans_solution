import math
import numpy as np


def second_recursive_strategy(data):
    """
    Do an exhaustive research of every possible world and return the max reward
    By storing all the leaf so not doing an np max at each node

    :param data: Numpy array of Rewards for every items
    :return: Max reward
    """
    ending_nodes = []
    def srs(worlds, counter):
        """
        define the recursive function
        :param worlds: List of possible next worlds
        :param counter: current reward
        :return: max reward from the current world
        """
        if len(worlds) == 0:
            return ending_nodes.append(counter)
        [srs(worlds=possible_worlds(world),
             counter=counter+world[0]) for world in worlds]
    srs([data], 0)
    return np.max(ending_nodes)

def possible_worlds(current_list):
    """
    Return every possible worlds from a current world
    :param current_list: Numpy array
    :return: List of Numpy array
    """
    return [current_list[i:] for i in range(1, 6) if i < current_list.shape[0]]
