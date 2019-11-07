import plan
import numpy as np


def crea(plans):
    actions = np.concatenate([p.actions for p in plans], axis=0)
    db = []
    for action in actions:
        tot_sum = np.zeros(len(action.oneHotprecondition[0]))
        for prec in action.oneHotprecondition:
            tot_sum = np.add(tot_sum, prec)
        for pos in action.oneHotpositiveEffects:
            tot_sum = np.add(tot_sum, pos)
        for neg in action.oneHotnegativeEffects:
            tot_sum = np.add(tot_sum, neg)
        tot_sum = tot_sum / (len(action.oneHotprecondition) + len(action.oneHotpositiveEffects) + len(action.oneHotnegativeEffects))
        db.append((tot_sum, action.oneHotAtction))
    return db