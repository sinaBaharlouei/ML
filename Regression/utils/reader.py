import scipy.io as sio


def read_mat_file(filename):
    mat_file = sio.loadmat(filename)
    data = mat_file['data']
    return data
