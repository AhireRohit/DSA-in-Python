myDict = {"Name" : "Rohit", "age" : 20, "college" : "MET"}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "Value does not exist!"
    
print(searchDict(myDict, "MET"))