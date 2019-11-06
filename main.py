import utils
import statistics
import numpy as np
import encoder
import save_arrays
import pickle
import oneHot
import natsort as na
import crea_istanze

if __name__ == '__main__':
    file1 = open("apn.obj", "rb")
    apn_list = pickle.load(file1)
    file2 = open("cit.obj", "rb")
    cit_list = pickle.load(file2)
    file3 = open("obj.obj", "rb")
    obj_list = pickle.load(file3)
    file4 = open("loc.obj", "rb")
    loc_list = pickle.load(file4)
    file5 = open("tru.obj", "rb")
    tru_list = pickle.load(file5)

    apn_list = na.natsorted(apn_list[1:])
    cit_list = na.natsorted(cit_list)
    obj_list = na.natsorted(obj_list[1:])
    tru_list = na.natsorted(tru_list)
    loc_list = na.natsorted(loc_list)

    folder = "SOL_files"
    print("inizio")
    plans = utils.get_plans(folder)
    # domains = utils.logistics_domains(folder)
    # statistics.init_statistics(domains)
    print("OK")
    # ave_arrays.save(domains, "domains.obj")
    # encoder.encoder(domains)
    code = oneHot.init(plans, apn_list, cit_list, obj_list, loc_list, tru_list)
    db = crea_istanze.crea(plans)
    print("fine")