import plan
import numpy as np


def crea(plans):
    actions = np.concatenate([p.actions for p in plans], axis=0)
    db = [(action.oneHotprecondition, action.oneHotAtction) for action in actions]
    return db