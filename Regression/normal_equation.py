from pylab import *
from utils import reader
import numpy as np
import matplotlib.pyplot as plt


def normal_equation(a, b):
    z = inv(dot(a.transpose(), a))
    return dot(dot(z, a.transpose()), b)


def cardinal(theta_vector):
    final_val = 0
    counter = 0
    for coefficient in theta_vector:
        if counter != 0:
            final_val += coefficient ** 2

        counter += 1

    return sqrt(final_val)


data = reader.read_mat_file("Data_HW1_95.mat")
x = data[0]
y = data[1]

m = len(x)

X = []
Y = []

n = 3  # degree
lam = 100  # lambda

for val in y:
    Y.append(val)
Y = np.matrix(Y)
Y = Y.transpose()

for item in x:
    row = []
    for d in range(0, n + 1):
        row.append(math.pow(item, d))
    X.append(row)

lambda_matrix = []
for j in range(0, n + 1):
    row = []
    for k in range(0, n + 1):
        if j == k and j != 0:
            row.append(1 * lam)
        else:
            row.append(0)
    lambda_matrix.append(row)

lambda_matrix = np.matrix(lambda_matrix)

X = np.matrix(X)
XT = X.transpose()

pro = dot(XT, X)
pro += lambda_matrix

inv_pro = inv(pro)
res1 = dot(inv_pro, XT)
final_res = dot(res1, Y)

theta = final_res.transpose()
theta = theta.tolist()
theta = theta[0]

new_x = linspace(0, 50, 200)

predicted_y = []
for item in new_x:
    i = 0
    val = 0
    for t in theta:
        val += t * item ** i
        i += 1

    predicted_y.append(val)

final_y = []
for item in x:
    i = 0
    val = 0
    for t in theta:
        val += t * item ** i
        i += 1

    final_y.append(val)

# compute MSE
MSE = 0
MAE = 0

differentiate = y - final_y
square_of_vector = differentiate * differentiate
absolute_vector = sqrt(square_of_vector)

for item in square_of_vector:
    MSE += item

for item in absolute_vector:
    MAE += item

MSE /= m
MAE /= m
RMSE = sqrt(MSE)

print "MSE is: ", MSE
print "RMSE is: ", RMSE
print "MAE is: ", MAE

plt.plot(x, y, "ro")
plt.plot(new_x, predicted_y, color="gold")
plt.show()

print theta
