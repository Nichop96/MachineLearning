import numpy as np
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
import keras
from matplotlib import pyplot as plt


def split(db):
    np.random.shuffle(db)
    dim = int(0.8*len(db))
    train, test = db[:dim], db[dim:]
    train_x = [x[0] for x in train]
    train_y = [y[1] for y in train]
    test_x = [x[0] for x in test]
    test_y = [y[1] for y in test]
    return np.array(train_x), np.array(train_y), np.array(test_x), np.array(test_y)


def get_net(dim):
    input = Input(shape=(dim,))
    d1 = Dense(20, activation="linear")(input)
    d2 = Dense(dim, activation="sigmoid")(d1)
    model = Model(input, d2)
    model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.1), loss='mse')
    return model


def get_k_fold_data(k, i, X, y):
    assert k > 1
    fold_size = X.shape[0] // k
    X_train, y_train = None, None
    for j in range(k):
        idx = slice(j * fold_size, (j + 1) * fold_size)
        X_part, y_part = X[idx, :], y[idx]
        if j == i:
            X_valid, y_valid = X_part, y_part
        elif X_train is None:
            X_train, y_train = X_part, y_part
        else:
            X_train = np.concatenate([X_train, X_part], axis=0)
            y_train = np.concatenate([y_train, y_part], axis=0)
    return X_train, y_train, X_valid, y_valid


def k_fold(k, X_train, y_train, num_epochs, batch_size):
    train_l_sum, valid_l_sum = 0, 0
    for i in range(k):
        data = get_k_fold_data(k, i, X_train, y_train)
        net = get_net(len(X_train[0]))
        history = net.fit(data[0], data[1], epochs=num_epochs, batch_size=batch_size, verbose=2,
                          validation_data=(data[2], data[3]))
        if i == 0:
            plt.plot(history.history['loss'])
            plt.plot(history.history['val_loss'])
            plt.title('model loss')
            plt.ylabel('loss')
            plt.xlabel('epoch')
            plt.legend(['train', 'test'], loc='upper left')
            plt.show()
    return train_l_sum / k, valid_l_sum / k