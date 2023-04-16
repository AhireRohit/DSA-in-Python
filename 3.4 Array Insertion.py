from array import*

arr1 = array('i', [1, 2, 3, 4, 5])

arr1.insert(4, 100)    # 4 is index where to insert ..... 100 is element
print(arr1)

# arr2 = array('d', [1.2, 1.5, 2.9, 8.9])
# print(arr2)


# When we insert element in start we have to move the rest elements to right. This is time consuming process. Here time complexity is ---> O(N) 
# When we insert element in end there is no movement. This is not time consuming process. Here time complexity is ---> O(1) 
# When we insert element in middle we have to move the rest elements to right. This is time consuming process. Here time complexity is ---> O(N) 
