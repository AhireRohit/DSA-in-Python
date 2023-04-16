import numpy as np

twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

print(twoDArray)


def searchInArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array [i][j] == value:
                return "The value is located at index " + str(i) + " " + str(j)
    return "The element does not exist in array."

print(searchInArray(twoDArray, 14))