import scipy.io as sio
import matplotlib.pyplot as plt
# Create random data with numpy


def read_mat_file(filename):
    return sio.loadmat(filename)

mat_file = read_mat_file("Data_HW1_95.mat")
data = mat_file['data']

lambda_values = [0, 10, 20, 50, 100]


# n = 2
theta_2 = [0.3657691798, 0.354783244724, 0.344438016637, 0.316731171375, 0.279287987694]

# n = 3
theta_3 = [0.873583755116, 0.730108136595, 0.627137242875, 0.44077566324, 0.294972726781]

# n = 7
theta_7 = [0.179682245088, 0.141322343811, 0.135260888925, 0.119974688668, 0.101006761437]

# plt.plot(lambda_values, theta_2, 'ro', color="green")
# plt.plot(lambda_values, theta_3, 'ro')
# plt.plot(lambda_values, theta_7, 'ro', color="gold")
# plt.show()
