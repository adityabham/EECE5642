import numpy as np
from scipy import signal

# filter
filter_matrix = np.array([[1, 2, 1],
                          [0, 0, 0],
                          [-1, -2, -1]])

# data
testing = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# padding
pad_data = np.pad(testing, (1, 1), 'edge')
print(pad_data)

result = signal.convolve2d(np.flip(filter_matrix), pad_data, mode='valid')
print(result)
