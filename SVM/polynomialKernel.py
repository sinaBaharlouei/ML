from sklearn import svm
from dataPreparation import get_data

train_data, train_data_target, validation_data, validation_data_target, test_data, test_data_target = get_data()

gamma_power_range = [0.001, 0.01, 0.1]
degree_range = range(1, 7)

for degree in degree_range:
    for gamma_power in gamma_power_range:
        clf = svm.SVC(kernel='poly', gamma=gamma_power, degree=degree, coef0=1)
        clf.fit(train_data, train_data_target)

        correct = incorrect = 0
        predicted = clf.predict(validation_data)
        for i in range(len(validation_data_target)):
            if predicted[i] == validation_data_target[i]:
                correct += 1
            else:
                incorrect += 1
        final_text = "degree:" + str(degree) + ", gamma:" + str(gamma_power) + " accuracy:" + str(float(correct) / (float(correct) + float(incorrect))) + "\n"
        print final_text
