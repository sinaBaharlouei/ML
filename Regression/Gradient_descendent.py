from pylab import *
from utils import reader

data = reader.read_mat_file("Data_HW1_95.mat")
X = data[0]
Y = data[1]

converged = False
iteration_counter = 0
m = X.shape[0]
alpha = 0.05
ep = 0.0001
max_iter = 300
momentum = 0.5

mean_x = mean_y = 0
std_x = std_y = 0

for data in X:
    mean_x += data
mean_x /= m

for data in X:
    std_x += pow(data - mean_x, 2)

std_x /= m
std_x = sqrt(std_x)

x = []

for data in X:
    x.append((data - mean_x) / std_x)

for data in Y:
    mean_y += data
mean_y /= m

for data in Y:
    std_y += pow(data - mean_y, 2)

std_y /= m
std_y = sqrt(std_y)

y = []

for data in Y:
    y.append((data - mean_y) / std_y)

# initial theta
t0 = 0
t1 = 0
t2 = 0
t3 = 0

v0 = v1 = v2 = v3 = 0

# total error, J(theta)
J = 0
for i in range(m):
    J += pow((t0 + t1 * x[i] + t2 * pow(x[i], 2) + t3 * pow(x[i], 3) - y[i]), 2)

J /= (2 * m)
print J

while not converged:

    grad0 = grad1 = grad2 = grad3 = 0

    # for each training sample, compute the gradient (d/d_theta j(theta))
    for i in range(m):
        grad0 += (t0 + t1 * x[i] + t2 * (x[i] * x[i]) + t3 * (x[i] * x[i] * x[i])) - y[i]
        grad1 += (t0 + t1 * x[i] + t2 * (x[i] * x[i]) + t3 * (x[i] * x[i] * x[i]) - y[i]) * x[i]
        grad2 += (t0 + t1 * x[i] + t2 * (x[i] * x[i]) + t3 * (x[i] * x[i] * x[i]) - y[i]) * (x[i] * x[i])
        grad3 += (t0 + t1 * x[i] + t2 * (x[i] * x[i]) + t3 * (x[i] * x[i] * x[i]) - y[i]) * (x[i] * x[i] * x[i])

    grad0 /= m
    grad1 /= m
    grad2 /= m
    grad3 /= m

    v0 = momentum * v0 + alpha * grad0
    v1 = momentum * v1 + alpha * grad1
    v2 = momentum * v2 + alpha * grad2
    v3 = momentum * v3 + alpha * grad3

    # update the theta_temp
    temp0 = t0 - v0
    temp1 = t1 - v1
    temp2 = t2 - v2
    temp3 = t3 - v3

    # update theta
    t0 = temp0
    t1 = temp1
    t2 = temp2
    t3 = temp3

    # mean squared error

    e = 0
    for i in range(m):
        e += pow((t0 + t1 * x[i] + t2 * pow(x[i], 2) + t3 * pow(x[i], 3) - y[i]), 2)

    e /= (2 * m)

    if abs(J - e) <= ep:
        print 'Converged, iterations: ', iteration_counter, '!!!'
        converged = True

    print J, e
    J = e  # update error
    iteration_counter += 1  # update iter

    if iteration_counter == max_iter:
        print 'Max interactions exceeded!'
        converged = True

print t0, t1, t2, t3

new_x = linspace(-2, 2, 200)

predicted_y = []
for item in new_x:
    predicted_y.append(t0 + t1 * item + t2 * item ** 2 + t3 * item ** 3)

plt.plot(x, y, "ro")
plt.plot(new_x, predicted_y, color="gold")
plt.show()
