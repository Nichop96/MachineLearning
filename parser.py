import numpy as np


if __name__ == '__main__':
    f = open("res\plan_pfile-51-0-1--I0-G0-n0.pddl_1.SOL", "r")
    lines = [line for line in f.readlines()]
    data = [l.split(";;(:metadata")[1] for l in lines if l.find(";;(:metadata") >= 0]
    init = data[0]
    actions = [act[:-2] for act in data[1:-1]]
    goals = data[len(data)-1]
    # now init contains the clean xml of the init part,
    # actions is an array that contains the clean xml of all the actions,
    # goals contains the clean xml of the goals part

