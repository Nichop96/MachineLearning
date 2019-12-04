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
                                    batch_size=128, epochs=10, verbose=2, validation_split=0.1)

        save_arrays.save(history, 'history')

        net.save('model')


    else:
        name = sys.argv[1]
        model = load_model(name)
        testing = open("mini_test", "rb")
        test = pickle.load(testing)
        test_x, test_y = neuralNet.split(test)
        res_y = model.predict(test_x)
        l = []
        for i in range(len(res_y[0])):
            pred = np.array([])
            correct = np.array([])
            for j in range(len(test_y)):
                pred = np.concatenate((pred, res_y[j][i][:]))
                correct = np.concatenate((correct, test_y[j][i][:]))
            tmp = np.zeros((2, len(pred)))
            tmp[0][:] = pred[:]
            tmp[1][:] = correct[:]
            l.append(tmp)
        print('fine')
