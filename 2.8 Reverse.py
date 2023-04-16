def reverse(array):
    for i in range(0,int(len(array)/2)):              # --> O(N)
        other = len(array)-i-1                        # --> O(1)
        temp = array[i]                               # --> O(1)
        array[i] = array[other]                       # --> O(1)
        array[other] = temp                           # --> O(1)
    print(array)                                      # --> O(1)

array = [1, 2, 3, 4, 5]
reverse(array)

# The final answer here is :- O(N) + O(1) + O(1) + O(1) + O(1) + O(1)
#                          =  O(N)
