# NumPy RuntimeWarning: invalid value encountered in divide

import numpy as np

np.seterr(divide='ignore', invalid='ignore')

arr1 = np.array([1, 2, 4, 6, 8])

arr2 = np.array([0, 1, 2, 3, 4])


result = np.divide(arr1, arr2)
print(result)