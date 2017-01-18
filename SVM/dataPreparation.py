import csv
import random
from math import sqrt


def normalize_vector(X, number_of_columns):
    m = len(X)
    for i in range(number_of_columns):
        mean_x = std_x = 0

        for data in X:
            mean_x += float(data[i])
        mean_x /= m

        for data in X:
            std_x += pow(float(data[i]) - mean_x, 2)

        std_x /= float(m)
        std_x = sqrt(std_x)

        for j in range(m):
            X[j][i] = ((float(X[j][i]) - mean_x) / std_x)

    return X


def get_data():
    with open('magic04.csv', 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    # target separation
    # g = 0, h = 1
    target = []
    number_of_data = len(your_list)
    number_of_features = len(your_list[0])
    for index in range(0, number_of_data):
        if your_list[index][number_of_features - 1] == 'g':
            target.append(0)
        else:
            target.append(1)

    [r.pop(number_of_features - 1) for r in your_list]

    your_list = normalize_vector(your_list, 10)

    # sampling
    number_of_data = len(your_list)
    x = []
    for i in range(0, number_of_data):
        x.append(i)

    random.shuffle(x)

    number_of_test_data = number_of_data / 10

    test_data_indices = x[:number_of_test_data]
    validation_data_indices = x[number_of_test_data:2 * number_of_test_data]

    test_data = []
    test_data_actual_target = []
    train_data = []
    train_data_target = []
    validation_data = []
    validation_data_target = []

    for index in range(number_of_data):
        if index in test_data_indices:
            test_data.append(your_list[index])
            test_data_actual_target.append(target[index])

        elif index in validation_data_indices:
            validation_data.append(your_list[index])
            validation_data_target.append(target[index])

        else:
            train_data.append(your_list[index])
            train_data_target.append(target[index])

    return train_data, train_data_target, validation_data, validation_data_target, test_data, test_data_actual_target
