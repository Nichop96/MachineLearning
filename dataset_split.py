import numpy as np
import pickle
import save_arrays
import natsort as na
import utils
import oneHot
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
        plans = utils.get_plans(folder)
        oneHot.init(plans, apn_list, cit_list, obj_list, loc_list, tru_list)
        db = crea_istanze.crea(plans)

        np.random.shuffle(db)
        dim1 = int(0.8 * len(db))
        dim2 = int(0.1 * len(db))
        train, test = db[:dim1], db[dim1:]
        train, validation = train[dim2:], train[:dim2]
        save_arrays.save(train, "training_set")
        save_arrays.save(test, "test_set")
        save_arrays.save(validation, "validation_set")
        print('dataset created')