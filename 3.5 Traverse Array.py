from array import*

arr1 = array('i', [1, 2, 3, 4, 5])

# arr1.insert(4, 100)    
# print(arr1)

def traverseArray(array):            
    for i in array:     # --> O(N)
        print(i)        # --> O(1)                

print(traverseArray(arr1))