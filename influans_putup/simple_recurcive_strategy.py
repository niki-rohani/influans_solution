import math
import numpy as np

def simple_recursive_strategy(data):
    def srs(worlds, counter):
        if len(worlds) == 0:
            return counter
        return np.max([srs(worlds=possible_worlds(world),
                           counter=counter+world[0]) for world in worlds])
    return srs([data], 0)

def possible_worlds(current_list):
    return [current_list[i:] for i in range(1, 6) if i < current_list.shape[0]]
