import numpy as np
import plan


if __name__ == '__main__':
    # file = sys.argv[1]
    file = "plan_pfile-83-1-2--I8-G6-n30.pddl_1.SOL" #for debugging, use command line arguments
    p = plan.Plan(file)
    # now init contains the clean xml of the init part,
    # actions is an array that contains the clean xml of all the actions,
    # goals contains the clean xml of the goals part
    print("test")
