import csv
import random
from math import cos, sqrt
from utils import find_mode
from DrawChart import draw_chart


def find_k(train_data_array, target_data, data_index, distance_type):
    given_data_vector = train_data_array[data_index]
    target_value = target_data[data_index]
    distance_vec = []
    for i in range(len(train_data_array)):
        if i != data_index:
            dist = find_distance(train_data_array[i], given_data_vector, distance_type)
            distance_vec.append((i, dist))

    sorted_distance_vector = sorted(distance_vec, key=lambda x: x[1])
    for selected_k in range(1, 9, 2):
        candidates = []
        for counter in range(selected_k):
            ind = sorted_distance_vector[counter][0]
            candidates.append(target_data[ind])

        # print candidates
        predicted = find_mode(candidates)
        # print "--------"
        # print predicted
        # print target_value
        # print "--------"
        if target_value == predicted:
            # print "hello"
            return selected_k
    return selected_k


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

    data_minimum_k_list = []
    for counter in range(len(sample_train_data)):
        k = find_k(sample_train_data, sample_train_target, counter, distance_type)
        data_minimum_k_list.append((counter, k))

    for item in test_data:
        # find nearest neighbour
        distance_vector = []
        for counter in range(len(sample_train_data)):
            distance = find_distance(item, sample_train_data[counter], distance_type)
            distance_vector.append((counter, distance))

        sorted_distance_vector = sorted(distance_vector, key=lambda x: x[1])

        appropriate_k = 0
        nearest_neighbour = sorted_distance_vector[0]
        for data in data_minimum_k_list:
            if nearest_neighbour[0] == data[0]:
                appropriate_k = data[1]

        candidates = []
        for counter in range(appropriate_k):
            ind = sorted_distance_vector[counter][0]
            candidates.append(sample_train_target[ind])
        predicted = find_mode(candidates)
        test_data_predicted_target.append(predicted)

    for i1 in range(len(test_data_predicted_target)):
        if test_data_predicted_target[i1] == test_data_actual_target[i1]:
            correct_answers += 1
        else:
            wrong_answers += 1

    # print "percentage:" + str(percentage) + "%"
    # print "correct_answers:" + str(correct_answers)
    # print "wrong answers:" + str(wrong_answers)
    # print "test data length:" + str(len(test_data))
    # print "train data length:" + str(len(sample_train_data))
    precision = float(correct_answers) / float(correct_answers + wrong_answers)
    # print "precision: " + str(precision)
    # print data_minimum_k_list
    # print "-------------------------------------------------------"
    return precision


with open('glass.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

target = []
number_of_data = len(your_list)
number_of_features = len(your_list[0])
for i in range(0, number_of_data):
    target.append(your_list[i][number_of_features - 1])

[r.pop(number_of_features - 1) for r in your_list]
[r.pop(0) for r in your_list]


x = []
for i in range(0, number_of_data):
    x.append(i)

# sampling
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