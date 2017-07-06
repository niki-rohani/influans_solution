import math
import numpy as np

world_visited = 0

def heuristic_recursive_strategy(data):
    """
    Do an heuristic research to reach the first positive value and then redo same and return the max reward
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

    counter = data[0]
    positive_values = np.where(data[1:] >= 0)[0]
    if positive_values.shape[0] == 0:
        return srs([data], 0)
    positive_values += 1

    # print(" positives values : " + str(data[positive_values]))

    for i in range(positive_values.shape[0]):
        prec = 0
        bias = counter
        if i > 0:
            prec = positive_values[i-1]
            bias = data[positive_values[i-1]]

        data_neg = data[prec:positive_values[i]+1]
        if data_neg.shape[0] == 0:
            data_neg = data[prec+1:]

        # print("positive data :" + str(data_neg))

        if data_neg.shape[0] > 0:
            counter = srs([data_neg], counter - bias)

    bias = data[positive_values[-1]]
    data_neg = data[positive_values[-1]:]
    # print("positive data :" + str(data_neg))
    if data_neg.shape[0] > 1:
        counter = srs([data_neg], counter - bias)

    print("World visited = " + str(world_visited))

    return counter

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

def next_positive_value(current_list):
    """
    :param current_list:
    :return:
    """
    positive_values = np.where(current_list >= 0)[0]
    if positive_values.shape[0] > 0:
        return current_list[:positive_values[0]+1]
    return current_list

