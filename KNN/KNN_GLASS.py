import csv
import random
from math import sqrt, cos
from utils import find_mode
from DrawChart import draw_chart


def get_sample(data_list, target_list, percentage):
    shuffle_set = []
    for n in range(0, len(data_list)):
        shuffle_set.append(n)
    # sampling
    random.shuffle(shuffle_set)
    number_of_items = len(data_list) * percentage / 100
    data_indices = shuffle_set[:number_of_items]

    final_array = []
    final_target = []
    for n in range(len(data_list)):
        if n in data_indices:
            final_array.append(data_list[n])
            final_target.append(target_list[n])

    return final_array, final_target


def find_distance(vec1, vec2, dist_type):
    dist = 0
    length = len(vec1)
    if length != len(vec2):
        return 99999999

    vec1_size = vec2_size = 0

    for ind in range(length):
        if dist_type == "Euclidean":
            dist += (float(vec1[ind]) - float(vec2[ind])) * (float(vec1[ind]) - float(vec2[ind]))
        elif dist_type == "Manhattan":
            dist += abs(float(vec1[ind]) - float(vec2[ind]))
        else:
            dist += float(vec1[ind]) * float(vec2[ind])
            vec1_size += float(vec1[ind]) * float(vec1[ind])
            vec2_size += float(vec2[ind]) * float(vec2[ind])

    if dist_type == "Cosine":
        dist = cos(float(dist) / (sqrt(float(vec1_size)) * sqrt(float(vec2_size))))
    return dist


def calculate(percentage, distance_type):
    sample_train_data, sample_train_target = get_sample(train_data, train_data_target, percentage)
    correct_answers = 0
    wrong_answers = 0

    test_data_predicted_target = []

    for item in test_data:
        distance_vector = []
        for counter in range(len(sample_train_data)):
            distance = find_distance(item, sample_train_data[counter], distance_type)
            distance_vector.append((counter, distance))

        sorted_distance_vector = sorted(distance_vector, key=lambda x: x[1])
        candidates = []
        for counter in range(k):
            ind = sorted_distance_vector[counter][0]
            candidates.append(sample_train_target[ind])
        predicted = find_mode(candidates)
        test_data_predicted_target.append(predicted)

    for i1 in range(len(test_data_predicted_target)):
        if test_data_predicted_target[i1] == test_data_actual_target[i1]:
            correct_answers += 1
        else:
            wrong_answers += 1

    precision = float(correct_answers) / float(correct_answers + wrong_answers)
    # print "percentage:" + str(percentage) + "%"
    # print "correct_answers:" + str(correct_answers)
    # print "wrong answers:" + str(wrong_answers)
    # print "test data length:" + str(len(test_data))
    # print "train data length:" + str(len(sample_train_data))
    # print "precision: " + str(precision)
    # print "-------------------------------------------------------"
    return precision


with open('glass.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

k = 3
target = []
number_of_data = len(your_list)
number_of_features = len(your_list[0])
for i in range(0, number_of_data):
    target.append(your_list[i][number_of_features - 1])

[r.pop(number_of_features - 1) for r in your_list]
[r.pop(0) for r in your_list]

# sampling
x = []
for i in range(0, number_of_data):
    x.append(i)

random.shuffle(x)

number_of_test_data = 25

test_data_indices = x[:number_of_test_data]

test_data = []
test_data_actual_target = []
train_data = []
train_data_target = []

for i in range(0, number_of_data):
    if i in test_data_indices:
        test_data.append(your_list[i])
        test_data_actual_target.append(target[i])
    else:
        train_data.append(your_list[i])
        train_data_target.append(target[i])

percentage_array = []
precision_array = []
for number in range(10, 110, 10):
    precision_rate = 0
    for index in range(10):
        precision_rate += calculate(number, "Euclidean")

    precision_rate /= 10
    percentage_array.append(number)
    precision_array.append(precision_rate)
    print (number, precision_rate)

draw_chart(percentage_array, precision_array)

# K
K_array = []
precision_array = []
for k in range(1, 45, 2):
    precision_rate = 0
    for index1 in range(20):
        precision_rate += calculate(100, "Euclidean")

    precision_rate /= 20
    K_array.append(k)
    precision_array.append(precision_rate)
    print (k, precision_rate)

draw_chart(K_array, precision_array)

"""
# Distances
for dis_type in ("Euclidean", "Manhattan", "Cosine"):
    percentage_array = []
    precision_array = []
    precision_rate = 0
    for index in range(20):
        precision_rate += calculate(100, dis_type)
    precision_rate /= 20
    print dis_type + ": " + str(precision_rate)
"""