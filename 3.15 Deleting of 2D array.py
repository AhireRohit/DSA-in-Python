import numpy as np

twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
print(twoDArray)

newArray = np.delete(twoDArray, 1, axis=1)
print(newArray)