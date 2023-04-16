def printPairs(array):
    for i in array:                                                 # --> O(N^2)
        for j in array:                                             # --> O(N)
            print(str(i) + "," + str(j))                            # --> O(1)

array = [12, 8, 2, 15, 1, 47]
print(printPairs(array))

# The final answer here is :- O(N^2) + O(N) + O(1)
#                          =  O(N^2) + O(1)
#                          =  O(N^2)