import math
import numpy as np


world_visited = 0

def simple_recursive_strategy(data):
    """
    Do an exhaustive research of every possible world and return the max reward
    :param data: Numpy array of Rewards for every items
    :return: Max reward
    """
    def srs(worlds, counter):
        """
        define the recursive function
        :param worlds: List of possible next worlds
        :param counter: current reward
        :return: max reward from the current world
        """
        if len(worlds) == 0:
            return counter
        return np.max([srs(worlds=possible_worlds(world),
                           counter=counter+world[0]) for world in worlds])

    srs = srs([data], 0)
    print("World visited = " + str(world_visited))
    return srs

def possible_worlds(current_list):
    """
    Return every possible worlds from a current world
    :param current_list: Numpy array
    :return: List of Numpy array
    """
    global world_visited
    possible_worlds = [current_list[i:] for i in range(1, 6) if i < current_list.shape[0]]
    world_visited += len(possible_worlds)
    return possible_worlds
