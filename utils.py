import plan
import os
import logistic_domain


def get_plans(folder):
    plan_list = [plan.Plan(folder + "/" + file) for file in os.listdir("SOL_files") if file.endswith(".SOL")]
    return plan_list


def logistics_domains(folder):
    domains_list = [logistic_domain.LogisticDomain(folder + "/" + file) for file in os.listdir("SOL_files") if file.endswith(".pddl")]
    return domains_list
