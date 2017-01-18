from sklearn import svm
from dataPreparation import get_data

train_data, train_data_target, validation_data, validation_data_target, test_data, test_data_target = get_data()

# C:32, gamma:0.1 accuracy:0.871976866456
clf = svm.SVC(kernel='rbf', C=32, gamma=0.1)
clf.fit(train_data, train_data_target)

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
