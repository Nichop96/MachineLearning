import numpy as np

def split_name_action(action):
    array = action.strip().split(" ")
    return array

def oneHot_action(name_action, ACTIONS):
    index = -1
    for id, val in enumerate(ACTIONS):
        if name_action == val:
            index = id
    if index != -1:
        array = []
        for i in range(7):
            if i == index:
                array.append(1)
            else:
                array.append(0)
        return array
    return -1


def init(plans):
    ACTIONS = ["LOAD-TRUCK", "UNLOAD-TRUCK", "DRIVE-TRUCK", "LOAD-AIRPLANE", "UNLOAD-AIRPLANE", "FLY-AIRPLANE"]
    NUMBER_ACTIONS = 6
    for p in plans:
        for action in p.actions:
            array = split_name_action(action.name)
            print(array[0],oneHot_action(array[0],ACTIONS))
