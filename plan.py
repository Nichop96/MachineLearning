import numpy as np
import xml.etree.ElementTree as ET


class Plan:
    def __init__(self, plan_description):
        f = open(plan_description, "r")
        lines = [line for line in f.readlines()]
        data = [l.split(";;(:metadata")[1] for l in lines if l.find(";;(:metadata") >= 0]
        init_root = ET.fromstring(data[0])
        goals_root = ET.fromstring(data[len(data) - 1])
        self.initial_state = [child.text for child in init_root]
        self.actions = [act[:-2] for act in data[1:-1]]
        self.goals = [child.text for child in goals_root]


