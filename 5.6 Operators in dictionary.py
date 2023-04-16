myDict = {"Name" : "Rohit", "age" : 20, "college" : "MET", "birth" : 2002, "hobby" : "Anime"}

print("birth" in myDict)               # in operator --> used to check if key available in dictionary. Accessed using key ... cannot be accessed using values. 
print(2002 in myDict.values())         # accessing using values.

for key in myDict:
    print(key)
    print(key, myDict[key])


# If all true --> True
# If all false --> False
# If one true other false --> False
# If one false other true --> False
# Empty dictionary --> True

newDict = {1 : True, 2 : True}

print(all(myDict))

print(len(myDict))                     # length

maxDict = {"z" : 1, "a" : 3}

print(sorted(maxDict))
print(sorted(maxDict, reverse = True))