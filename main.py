import utils
import statistics
import numpy as np
import encoder
import save_arrays

if __name__ == '__main__':
    # file = sys.argv[1]
    # file = "plan_pfile-51-0-1--I0-G0-n0.pddl_1.SOL" #for debugging, use command line arguments
    # p = plan.Plan(file)
    folder = "C:\\Users\\user\\Downloads\\logistics\\cb_problems"
    #folder = "SOL_files"
    print("inizio")
    #plans = utils.get_plans(folder)
    domains = utils.logistics_domains(folder)
    #statistics.init_statistics(domains)
    print("OK")
    #ave_arrays.save(domains, "domains.obj")
    encoder.encoder(domains)
    print("fine")
