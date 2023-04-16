from array import*

arr1 = array('i', [1, 2, 3, 4, 5])

def accessArray(array, index):
    if index > len(array):
        print("There is no element in this index")
    else:
        print(array[index])


accessArray(arr1, 2)