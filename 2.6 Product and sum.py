def foo(array):
    sum = 0                                                                                    # --> O(1)
    product = 1                                                                                # --> O(1)

    for i in array:                                                                            # --> O(N)
        sum += i                                                                               # --> O(!)

    for i in array:                                                                            # --> O(N)
        product *= i                                                                           # --> O(1)
    print("Sum = " + str(sum) + ", Product = " + str(product))                                 # --> O(1)

array = [12, 85, 2]
print(foo(array))

# The final answer here is :- O(1) + O(1) + O(N) + O(1) + O(N) + O(1) + O(1)
#                          =  O(1) + O(N) + O(N)
#                          =  O(N)