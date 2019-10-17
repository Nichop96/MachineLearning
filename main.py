import utils


if __name__ == '__main__':
    # file = sys.argv[1]
    # file = "plan_pfile-51-0-1--I0-G0-n0.pddl_1.SOL" #for debugging, use command line arguments
    # p = plan.Plan(file)
    folder = "SOL_files"
    plans = utils.get_plans(folder)
    domains = utils.logistics_domains(folder)
    print("test")
