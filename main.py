import utils
import numpy as np
import pickle
import oneHot
import natsort as na
import crea_istanze
import neuralNet
from matplotlib import pyplot as plt
import save_arrays
import sys
from keras.models import load_model


if __name__ == '__main__':

    if len(sys.argv) == 1:

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
        # domains = utils.logistics_domains(folder)
        # save_arrays.save(domains, "domains.obj")
        # encoder.encoder(domains)
        # code = oneHot.init(plans, apn_list, cit_list, obj_list, loc_list, tru_list)
        # db = crea_istanze.crea(plans)
        #
        # neuralNet.save_db(db)

        training = open("training_set", "rb")
        train = pickle.load(training)

        testing = open("test_set", "rb")
        test = pickle.load(testing)


        net = neuralNet.get_net(len(train[0][0]))

        train_x, train_y = neuralNet.split(train)

        test_x, test_y = neuralNet.split(test)

        print(net.summary())
        history = net.fit(train_x, {'action_type': train_y[0], 'type1': train_y[1], 'param1': train_y[2], 'type2': train_y[3],
                                    'param2': train_y[4], 'type3': train_y[5], 'param3': train_y[6], 'type4': train_y[7], 'param4': train_y[8]},
                                    batch_size=128, epochs=60, verbose=2)

        plt.plot(history.history['loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        # score = net.evaluate(test_x, test_y)
        net.save("model")
        # print(score)

    else:
        name = sys.argv[1]
        model = load_model(name)
        testing = open("test_set", "rb")
        test = pickle.load(testing)
        test_x, test_y = neuralNet.split(test)
        res_y = model.predict(test_x)
        l = []
        for i in range(len(res_y)):
            tmp = np.zeros((2, len(test_y[0])))
            tmp[0][:] = res_y[i][:]
            tmp[1][:] = test_y[i][:]
            l.append(tmp)
        a = np.sum(np.power(np.absolute(np.subtract(tmp[0], tmp[1])), 2))/len(tmp[0])
        print('fine')
