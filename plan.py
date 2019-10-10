import numpy as np


class Plan:
    def __init__(self, plan_description):
        f = open(plan_description, "r")
        lines = [line for line in f.readlines()]
        data = [l.split(";;(:metadata")[1] for l in lines if l.find(";;(:metadata") >= 0]
        self.init = data[0]
        self.actions = [act[:-2] for act in data[1:-1]]
        self.goals = data[len(data) - 1]
