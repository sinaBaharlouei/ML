from sklearn import svm
from dataPreparation import get_data
import random
train_data, train_data_target, validation_data, validation_data_target, test_data, test_data_target = get_data()

gamma_power_range = range(-2, 2)
c_power_range = range(6, 9)

my_file = open("rbf_result2.txt", "w")
for k in range(20):
    c = pow(2, random.uniform(-2, 8))
    gamma = pow(10, random.uniform(-10, 10))
    clf = svm.SVC(kernel='rbf', C=c, gamma=gamma)
    clf.fit(train_data, train_data_target)

    correct = incorrect = 0
    predicted = clf.predict(validation_data)
    for i in range(len(validation_data_target)):
        if predicted[i] == validation_data_target[i]:
            correct += 1
        else:
            incorrect += 1
    final_text = "C:" + str(pow(2, c)) + ", gamma:" + str(pow(10, gamma)) + " accuracy:" + str(float(correct) / (float(correct) + float(incorrect))) + "\n"
    my_file.write(final_text)
