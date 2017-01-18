import scipy.io as sio
import matplotlib.pyplot as plt
# Create random data with numpy


def read_mat_file(filename):
    return sio.loadmat(filename)

mat_file = read_mat_file("Data_HW1_95.mat")
data = mat_file['data']
plt.plot(data[0], data[1], 'ro')
plt.show()

print data[0]
print data[1]
