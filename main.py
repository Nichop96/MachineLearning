import numpy as np
import plan
import action
import sys
import os


if __name__ == '__main__':
    # file = sys.argv[1]
    # file = "plan_pfile-51-0-1--I0-G0-n0.pddl_1.SOL" #for debugging, use command line arguments
    # p = plan.Plan(file)
    folder = "SOL_files"
    plan_list = [plan.Plan(folder + "/" + file) for file in os.listdir("SOL_files") if file.endswith(".SOL")]
    print("test")
