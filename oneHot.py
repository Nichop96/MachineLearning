import numpy as np

def split_name_action(action):
    array =  action.strip().split(" ")
    return  array

def init(plans):
    for p in plans:
        for action in p.actions:
            array = split_name_action(action.name)
