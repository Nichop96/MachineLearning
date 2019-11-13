import utils
import numpy as np
import pickle
import oneHot
import natsort as na
import crea_istanze
import neuralNet
from matplotlib import pyplot as plt


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
    net = neuralNet.get_net(len(db[0][0]))
    train_x, train_y, test_x, test_y = neuralNet.split(db)
    # train_l, valid_l = neuralNet.k_fold(5, train_x, train_y, 60, 128)
    # print('%d-fold validation: avg train rmse: %f, avg valid rmse: %f'
    #       % (5, train_l, valid_l))

    print(net.summary())
    history = net.fit(train_x, train_y, batch_size=128, epochs=60, verbose=2, validation_data=(test_x, test_y))
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    score = net.evaluate(test_x, test_y)
    print(score)
    print("fine")