from sklearn import svm
from dataPreparation import get_data

train_data, train_data_target, validation_data, validation_data_target, test_data, test_data_target = get_data()

r_dictionary = range(-3, 0)
gamma_range = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100]

for r in r_dictionary:
    for gamma in gamma_range:
        clf = svm.SVC(kernel='sigmoid', gamma=gamma, coef0=r)  # sigmoid: r by coef0
        clf.fit(train_data, train_data_target)

        correct = incorrect = 0
        predicted = clf.predict(validation_data)
        for i in range(len(validation_data_target)):
            if predicted[i] == validation_data_target[i]:
                correct += 1
            else:
                incorrect += 1

        print correct
        print incorrect
        print "r = ", r, ", gamma = ", gamma
        print "accuracy = ", float(correct) / (float(correct) + float(incorrect))
        print '--------------------------------------------------------'
