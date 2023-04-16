myDict = {"Name" : "Rohit", "age" : 20, "college" : "MET", "birth" : 2002, "hobby" : "Anime"}

print(myDict.pop("Name"))           # returns value
print(myDict)                  

print(myDict.popitem())             # returns key and value
print(myDict)

myDict.clear()                      # clears everything
print(myDict)

# del keyword is used to delete spectific pair orwhole dictionary

del myDict                            # this statement deletes whole dictionary

 