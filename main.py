import utils
import statistics
import numpy as np

if __name__ == '__main__':
    # file = sys.argv[1]
    # file = "plan_pfile-51-0-1--I0-G0-n0.pddl_1.SOL" #for debugging, use command line arguments
    # p = plan.Plan(file)
    folder = "cb_problems"
    print("test")
    #plans = utils.get_plans(folder)
    domains = utils.logistics_domains(folder)
    statistics.init_statistics(domains)
    print("test")
