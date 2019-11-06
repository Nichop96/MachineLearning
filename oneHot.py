import numpy as np

NUMBER_ACTIONS = 12
MAX_OBJECTS = 103
ACTIONS = ["LOAD-TRUCK", "UNLOAD-TRUCK", "DRIVE-TRUCK", "LOAD-AIRPLANE", "UNLOAD-AIRPLANE", "FLY-AIRPLANE","at","in","not at", "not in"]
TYPES_OBJECT = ["APN", "CIT", "OBJ", "LOC", "TRU"]

def split_name_action(action):
    array = action.strip().split(" ")
    return array

def oneHot_parameter(parameter, apn_list, cit_list, obj_list, loc_list, tru_list):
    type = np.zeros(len(TYPES_OBJECT))
    if "APN" in parameter:
        type[0] = 1
        return np.concatenate([type, oneHot(parameter, apn_list, MAX_OBJECTS)])
    if "CIT" in parameter:
        type[1] = 1
        return np.concatenate([type, oneHot(parameter, cit_list, MAX_OBJECTS)])
    if "OBJ" in parameter:
        type[3] = 1
        return np.concatenate([type, oneHot(parameter, loc_list, MAX_OBJECTS)])
    if "TRU" in parameter:
        type[4] = 1
        return np.concatenate([type, oneHot(parameter, tru_list, MAX_OBJECTS)])

def invalid_encode():
    array = np.zeros(len(TYPES_OBJECT)+MAX_OBJECTS)
    array[len(TYPES_OBJECT)] = 1
    return array

def oneHot(parameter, array, max_length):
    index = -1
    for id, val in enumerate(array):
        if parameter == val:
            index = id
    if index != -1:
        array = np.zeros(max_length)
        array[index] = 1
        return array
    return -1

def oneHotAction(action, apn_list, cit_list, obj_list, loc_list, tru_list):
    array = split_name_action(action)
    code = []
    code.append(oneHot(array[0], ACTIONS, NUMBER_ACTIONS))
    for i in range(1, len(array)):
        code.append(oneHot_parameter(array[i], apn_list, cit_list, obj_list, loc_list, tru_list))
    for i in range(len(array) - 1, 4):
        code.append(invalid_encode())
    return code

def init(plans, apn_list, cit_list, obj_list, loc_list, tru_list):
    code = []
    for p in plans:
        for action in p.actions:
            code.append(oneHotAction(action.name, apn_list, cit_list, obj_list, loc_list, tru_list))
    return code