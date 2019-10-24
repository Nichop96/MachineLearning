import  logistic_domain
import save_arrays


def encoder(domains_list):
        apn_list = []
        for dom in domains_list:
            for a in dom.apn:
                if a not in apn_list:
                    apn_list.append(a)
        save_arrays.save(apn_list, "apn.obj")
        cit_list = []
        for dom in domains_list:
            for c in dom.cit:
                if c not in cit_list:
                    cit_list.append(c)
        save_arrays.save(cit_list, "cit.obj")
        loc_list = []
        for dom in domains_list:
            for l in dom.loc:
                if l not in loc_list:
                    loc_list.append(l)
        save_arrays.save(loc_list, "loc.obj")
        obj_list = []
        for dom in domains_list:
            for o in dom.obj:
                if o not in obj_list:
                    obj_list.append(o)
        save_arrays.save(obj_list, "obj.obj")
        tru_list = []
        for dom in domains_list:
            for t in dom.tru:
                if t not in tru_list:
                    tru_list.append(t)
        save_arrays.save(tru_list, "tru.obj")