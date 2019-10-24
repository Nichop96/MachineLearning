import numpy as np

NUMBER_ACTIONS = 6
ACTIONS = ["LOAD-TRUCK", "UNLOAD-TRUCK", "DRIVE-TRUCK", "LOAD-AIRPLANE", "UNLOAD-AIRPLANE", "FLY-AIRPLANE"]

def split_name_action(action):
    array = action.strip().split(" ")
    return array

def oneHot_action(name_action):
    index = -1
    for id, val in enumerate(ACTIONS):
        if name_action == val:
            index = id
    if index != -1:
        array = []
        for i in range(NUMBER_ACTIONS):
            if i == index:
                array.append(1)
            else:
                array.append(0)
        return array
    return -1

def oneHot_parameter(parameter, apn_list, cit_list, obj_list, loc_list, tru_list):
    type = np.zeros(6)
    if "APN" in parameter:
        type[0] = 1
        return oneHot(parameter, apn_list), type
    if "CIT" in parameter:
        type[1] = 1
        return oneHot(parameter, cit_list)
    if "OBJ" in parameter:
        type[2] = 1
        return oneHot(parameter, obj_list)
    if "LOC" in parameter:
        type[3] = 1
        return oneHot(parameter, loc_list)
    if "TRU" in parameter:
        type[4] = 1
        return oneHot(parameter, tru_list)


def oneHot(parameter, array):
    index = -1
    for id, val in enumerate(array):
        if parameter == val:
            index = id
    if index != -1:
        #array = np.zeros(len(array))
        array = np.zeros(103)
        array[index] = 1
        return array
    return -1

def init(plans, apn_list, cit_list, obj_list, loc_list, tru_list):
    for p in plans:
        for action in p.actions:
            array = split_name_action(action.name)
            #print(array[0],oneHot_action(array[0]))
            print(array[1], oneHot_parameter(array[1], apn_list, cit_list, obj_list, loc_list, tru_list))
