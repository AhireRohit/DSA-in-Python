import numpy as np

twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

print(twoDArray)

newTWO = np.insert(twoDArray, 0, [[16, 17, 18]], axis=0)

def accessElement(array, rowIndex, columnIndex):
    if rowIndex >= len(array) and columnIndex >= len(array):
        print('Incorrect Index')
    else:
        print(array[rowIndex][columnIndex])

accessElement(twoDArray, 1, 2)

# Time and space complexity for above code is O(1)
