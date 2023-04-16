tuple = ("a", "b", "c", "d")

def searchTuple(tuple, element):
    for i in tuple:
        if i == element:
            return tuple.index(i)
    return "The element does not exist!"

print(searchTuple(tuple, "p"))