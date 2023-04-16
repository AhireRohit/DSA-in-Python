from array import*

array = [1, 2, 3, 4, 5]

# transverse

for i in array:
    print(i)

# append

print(array[0])
array.append(101)
print(array)

# insert

array.insert(2, 50)
print(array)


# Extend an array

array2 = [6, 7, 8, 9, 10]
array.extend(array2)
print(array)

# Add list to array

list = [85, 89, 90]
array.extend(list)
print(array)

# remove from array

array.remove(90)
print(array)

# remove last element

array.pop()
print(array)

# Fetch any element using index

print(array[8])

# reverse the array

array.reverse()
print(array)


# Occurence of an element

print(array.count(2))

