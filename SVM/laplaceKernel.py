from math import exp
from sklearn import svm
from dataPreparation import get_data
import numpy as np
import gaussianKernel as gk


def gaussianKernelGramMatrix(X1, X2, K_function=gk.gaussianKernel, sigma=0.1):
    """(Pre)calculates Gram Matrix K"""

    gram_matrix = np.zeros((X1.shape[0], X2.shape[0]))
    for i, x1 in enumerate(X1):
        for j, x2 in enumerate(X2):
            gram_matrix[i, j] = K_function(x1, x2, sigma)
    return gram_matrix

train_data, train_data_target, validation_data, validation_data_target, test_data, test_data_target = get_data()


# C:32, gamma:0.1 accuracy:0.871976866456
clf = svm.SVC(kernel='precomputed', C=16)
clf.fit(gaussianKernelGramMatrix(train_data, train_data), train_data_target)

correct = incorrect = 0
predicted = clf.predict(train_data)
for i in range(len(train_data_target)):
    if predicted[i] == train_data_target[i]:
        correct += 1
    else:
        incorrect += 1

print "train data:"
print "correct:", correct, ", incorrect:", incorrect, ", accuracy:", float(correct) / float(correct + incorrect)
print "--------------------------------------------------"

correct = incorrect = 0
predicted = clf.predict(validation_data)
for i in range(len(validation_data_target)):
    if predicted[i] == validation_data_target[i]:
        correct += 1
    else:
        incorrect += 1

print "validation data:"
print "correct:", correct, ", incorrect:", incorrect, ", accuracy:", float(correct) / float(correct + incorrect)
print "--------------------------------------------------"

correct = incorrect = 0
predicted = clf.predict(test_data)
for i in range(len(test_data)):
    if predicted[i] == test_data_target[i]:
        correct += 1
    else:
        incorrect += 1

print "test data:"
print "correct:", correct, ", incorrect:", incorrect, ", accuracy:", float(correct) / float(correct + incorrect)
print "--------------------------------------------------"
print("supports:", clf.n_support_)
