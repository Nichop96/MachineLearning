import  logistic_domain
import save_arrays
import numpy as np


def encoder(domains_list):
        apn_list = []
        for dom in domains_list:
            apn_list = apn_list + dom.apn
        apn_list = np.asanyarray(list(set(apn_list)))
        save_arrays.save(apn_list, "apn.obj")
        cit_list = []
        for dom in domains_list:
            cit_list = cit_list + dom.apn
        cit_list = np.asanyarray(list(set(cit_list)))
        save_arrays.save(cit_list, "cit.obj")
        loc_list = []
        for dom in domains_list:
            loc_list = loc_list + dom.apn
        loc_list = np.asanyarray(list(set(loc_list)))
        save_arrays.save(loc_list, "loc.obj")
        obj_list = []
        for dom in domains_list:
            obj_list = obj_list + dom.apn
        obj_list = np.asanyarray(list(set(obj_list)))
        save_arrays.save(obj_list, "obj.obj")
        tru_list = []
        for dom in domains_list:
            tru_list = tru_list + dom.apn
        tru_list = np.asanyarray(list(set(tru_list)))
        save_arrays.save(tru_list, "tru.obj")