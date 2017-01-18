from pylab import *
import csv
import random
import matplotlib.pyplot as plt
import numpy as np


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


def sigmoid(z):
    return float(1.0 / float((1.0 + math.exp(-1.0 * z))))


def h(theta, x):
    z = 0
    for i in xrange(len(theta)):
        z += float(x[i]) * theta[i]

    return sigmoid(z)


def cost_function(X, Y, theta):
    m = len(X)
    sum_of_errors = 0

    for i in xrange(m):
        xi = X[i]
        hi = h(theta, xi)
        error = 0

        if Y[i] == 1:
            error = Y[i] * math.log(hi)

        elif Y[i] == 0:
            error = (1 - Y[i]) * math.log(1 - hi)

        sum_of_errors += error

    j = (-1 / float(m)) * sum_of_errors
    print 'cost is ', j
    return j


def cost_function_derivative(X, Y, theta, j, alpha):
    sum_errors = 0
    m = len(Y)

    for i in xrange(m):
        xi = X[i]
        xij = float(xi[j])
        hi = h(theta, X[i])
        error = (hi - Y[i]) * xij
        sum_errors += error

    return (float(alpha) / float(m)) * sum_errors


def gradient_descent(X, Y, theta, alpha):
    m = len(Y)
    new_theta = []
    constant = alpha / m
    for j in xrange(len(theta)):
        dj = cost_function_derivative(X, Y, theta, j, alpha)
        new_theta_value = theta[j] - dj
        new_theta.append(new_theta_value)

    return new_theta


def logistic_regression(X, Y, alpha, theta, num_iteration):
    m = len(Y)
    for x in xrange(num_iteration):
        new_theta = gradient_descent(X, Y, theta, alpha)
        theta = new_theta
        if x % 100 == 0:
            cost_function(X, Y, theta)
            print 'theta ', theta

    print 'cost is ', cost_function(X, Y, theta)
    return theta


def validation(theta, test_data, test_target):
    pass


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

print your_list[0]
print target[0]

your_list = normalize_vector(your_list, 10)

# sampling
number_of_data = len(your_list)
x = []
for i in range(0, number_of_data):
    x.append(i)

random.shuffle(x)

number_of_test_data = number_of_data / 5

test_data_indices = x[:number_of_test_data]

test_data = []
test_data_actual_target = []
train_data = []
train_data_target = []

for index in range(number_of_data):
    if index in test_data_indices:
        test_data.append(your_list[index])
        test_data_actual_target.append(target[index])
    else:
        train_data.append(your_list[index])
        train_data_target.append(target[index])

# setting variables
initial_theta = [0.5, 0.28, 0, 0, 0, 0, 0, 0, 0, 0]
initial_alpha = 0.1
iterations = 500
learned_params = logistic_regression(train_data, train_data_target, initial_alpha, initial_theta, iterations)

ROC_TPR_array = []
ROC_FPR_array = []

score = 0

threshold_array = []

for index in range(1001):
    threshold_array.append(float(index) / float(1000))

print threshold_array

accuracy = 0

for item in threshold_array:
    tp = fp = tn = fn = 0

    for index in range(len(test_data)):

        prob = h(learned_params, test_data[index])
        predicted = 0
        if prob >= item:
            predicted = 1

        if predicted == 0 and test_data_actual_target[index] == 0:
            tp += 1
        elif predicted == 0 and test_data_actual_target[index] == 1:
            fp += 1
        elif predicted == 1 and test_data_actual_target[index] == 0:
            fn += 1
        elif predicted == 1 and test_data_actual_target[index] == 1:
            tn += 1

    if item == 0.5:
            accuracy = float(tp + tn) / float(tp + fn + fp + tn)
    ROC_TPR_array.append(float(tp) / float(tp + fn))
    ROC_FPR_array.append(float(fp) / float(fp + tn))

identity_line = np.linspace(0, 1, 1000)
plt.plot(identity_line, identity_line, color="black", linestyle="dashed", linewidth=1.0)

plt.plot(ROC_FPR_array, ROC_TPR_array, color="blue")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC Logistic regression')
plt.show()

print "accuracy:" + str(accuracy)
