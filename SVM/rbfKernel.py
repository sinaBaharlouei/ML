from sklearn import svm
from dataPreparation import get_data

train_data, train_data_target, validation_data, validation_data_target, test_data, test_data_target = get_data()

gamma_power_range = range(-2, 2)
c_power_range = range(6, 9)

my_file = open("rbf_result2.txt", "w")
for c_power in c_power_range:
    for gamma_power in gamma_power_range:
        clf = svm.SVC(kernel='rbf', C=pow(2, c_power), gamma=pow(10, gamma_power))
        clf.fit(train_data, train_data_target)

        correct = incorrect = 0
        predicted = clf.predict(validation_data)
        for i in range(len(validation_data_target)):
            if predicted[i] == validation_data_target[i]:
                correct += 1
            else:
                incorrect += 1
        final_text = "C:" + str(pow(2, c_power)) + ", gamma:" + str(pow(10, gamma_power)) + " accuracy:" + str(float(correct) / (float(correct) + float(incorrect))) + "\n"
        my_file.write(final_text)
